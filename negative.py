import cv2
# enter your image relative path here and replace "\" with "/"
neg_img = cv2.imread('neg_conv/sample_input.jpg')
if neg_img is None:
    print("Error: Could not read the image.")
else:
    # Convert negative to positive
    pos_img = 255 - neg_img

    save_path = 'positive2.jpg'
# Save the positive image
    cv2.imwrite(save_path, pos_img)
    print(f"Positive image saved as {save_path}.")
    # Display the positive image
    cv2.imshow('Positive Image', pos_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()