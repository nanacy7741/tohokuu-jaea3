import logging

import azure.functions as func


def main(inputblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {inputblob.name}\n"
                 f"Blob Size: {inputblob.length} bytes")
    logging.info(f"github actions setting !!!")
    outputblob.set(inputblob)
