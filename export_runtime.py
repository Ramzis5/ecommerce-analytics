"""Memory-conscious sales exports; called only after explicit preparation."""

from datetime import datetime
from io import BytesIO

import pandas as pd
from openpyxl import Workbook


SALES_EXCEL_COLUMNS = [
    "order_id", "product_name", "brand", "category", "department",
    "sale_price", "product_cost", "profit", "status", "country", "created_at",
]


def build_sales_excel(sales):
    """Stream rows into XLSX instead of retaining a workbook full of cells."""
    workbook = Workbook(write_only=True)
    sheet = workbook.create_sheet("Sales")
    sheet.append(SALES_EXCEL_COLUMNS)
    for row in sales[SALES_EXCEL_COLUMNS].itertuples(index=False, name=None):
        values = []
        for value in row:
            if pd.isna(value):
                value = None
            elif isinstance(value, (datetime, pd.Timestamp)):
                timestamp = pd.Timestamp(value)
                if timestamp.tzinfo is not None:
                    timestamp = timestamp.tz_convert("UTC").tz_localize(None)
                value = timestamp.to_pydatetime()
            values.append(value)
        sheet.append(values)
    with BytesIO() as output:
        workbook.save(output)
        return output.getvalue()
