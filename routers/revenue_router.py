from fastapi import APIRouter
from services.sales_service import SalesService
import sys

RevenueRouter = APIRouter(
    prefix="/revenue",
    tags=["items"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@RevenueRouter.get("/")
async def get_revenue():
    sales_service = SalesService()
    all_time_sales = sales_service.get_all(sys.maxsize)
    revenue = 0
    for sales_record in all_time_sales:
        revenue += sales_record.quantity * sales_record.sale_price
    return {"revenue": revenue}
