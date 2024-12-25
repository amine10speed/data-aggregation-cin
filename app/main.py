from fastapi import FastAPI, HTTPException
from app.aggregation import aggregate_data, export_to_json, export_to_csv

app = FastAPI()

@app.post("/aggregate/")
async def aggregate_endpoint(data: dict, export_format: str = "json"):
    """
    Endpoint to aggregate and export data.
    :param data: JSON containing extracted fields from previous microservices.
    :param export_format: Desired export format ("json" or "csv").
    :return: Success message and export file path.
    """
    try:
        # Aggregate data
        aggregated_data = aggregate_data(data)

        # Export data to the desired format
        if export_format == "json":
            export_to_json(aggregated_data)
            export_path = "output.json"
        elif export_format == "csv":
            export_to_csv(aggregated_data)
            export_path = "output.csv"
        else:
            raise HTTPException(status_code=400, detail="Unsupported export format")

        return {"message": "Data aggregated and exported successfully", "file": export_path}
    except Exception as e:
        return {"message": "Error during aggregation or export", "error": str(e)}
