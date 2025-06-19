import logging
import azure.functions as func

def main(inputBlob: func.InputStream, outputBlob: func.Out[str]):
    logging.info(f"Processing blob: {inputBlob.name}, Size: {inputBlob.length} bytes")

    # Dummy summarization for testing
    text = inputBlob.read().decode('utf-8', errors='ignore')
    summary = f"Summary for file {inputBlob.name}:\n\n{text[:500]}"

    outputBlob.set(summary)
