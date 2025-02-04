from fastapi import APIRouter, HTTPException, Path
import logfire

from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:

    with logfire.span("Create Summary"):
        logfire.info("Creating summary...")
        print("payload: ", payload)

        summary_id = await crud.post(payload)
        logfire.info("Summary created successfully with id: {summary_id}")
        response_object = {"id": summary_id, "url": payload.url}
        return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int = Path(..., gt=0)) -> SummarySchema:  # type: ignore
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.get("/", response_model=list[SummarySchema])
async def read_all_summaries() -> list[SummarySchema]:  # type: ignore
    return await crud.get_all()


@router.delete("/{id}/", response_model=SummaryResponseSchema)
async def remove_summary(id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    await crud.delete(id)
    return summary


@router.put("/{id}/", response_model=SummarySchema)
async def update_summary(
    payload: SummaryUpdatePayloadSchema, id: int = Path(..., gt=0)
) -> SummarySchema:
    with logfire.span("Update Summary"):
        logfire.info("Updating summary...")
        summary = await crud.put(id, payload)
        if not summary:
            logfire.error("Summary not found")
            raise HTTPException(status_code=404, detail="Summary not found")
        logfire.info("Summary updated successfully")
    return summary
