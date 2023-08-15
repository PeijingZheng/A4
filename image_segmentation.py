"""
This script provides functions related to image input and segmentation using the gdal library.

Author: peijing
Date: 2023--08--15
"""

import gdal

def read_image(filename):
    """
    Read an image file using the GDAL library.

    Args:
        filename (str): The path to the image file.

    Returns:
        ndarray: The image data as a NumPy array.
    """
    # Read the image using GDAL
    dataset = gdal.Open(filename)
    image_data = dataset.ReadAsArray()

    return image_data

def segment_image(image_data, threshold):
    """
    Segment an image based on a given threshold.

    Args:
        image_data (ndarray): The image data as a NumPy array.
        threshold (float): The threshold value for segmentation.

    Returns:
        ndarray: The segmented image data as a NumPy array.
    """
    # Perform image segmentation based on the threshold
    segmented_data = image_data > threshold

    return segmented_data

def save_segmentation_result(segmented_data, output_filename):
    """
    Save the segmentation result as an image file.

    Args:
        segmented_data (ndarray): The segmented image data as a NumPy array.
        output_filename (str): The desired path for the output file.
    """
    # Create a new GDAL dataset to save the segmentation result
    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(output_filename, segmented_data.shape[1], segmented_data.shape[0], 1, gdal.GDT_Byte)
    dataset.GetRasterBand(1).WriteArray(segmented_data)
    dataset.FlushCache()

    print("Segmentation result saved successfully.")


