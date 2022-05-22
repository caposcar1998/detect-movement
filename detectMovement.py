# import the opencv module
import cv2


def detectMovement():
    # capturing video
    video = cv2.VideoCapture("bobesponja.mp4")

    f = 0
    ancho = 722 
    largo = 406

    while video.isOpened():
        # to read frame by frame
        ret1, first_image = video.read()
        ret2, second_image = video.read()

        if ret1 and ret2:
            # find difference between two frames
            diff_images = cv2.absdiff(first_image, second_image)

            # to convert the frame to grayscale
            diff_gray = cv2.cvtColor(diff_images, cv2.COLOR_BGR2GRAY)


            # to get the binary image
            _, thresh_bin = cv2.threshold(diff_gray, 20, 255, cv2.THRESH_BINARY)

            # to find contours
            contours, _ = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.putText(first_image,str(f),(ancho-100,largo-50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255))

            # to draw the bounding box when the motion is detected
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                if cv2.contourArea(contour) > 300:
                    cv2.rectangle(first_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.cv2.circle(first_image, (x,y), radius=1, color=(0, 0, 255), thickness=-1)


            # display the output
            cv2.imshow("Detector activated...", first_image)
            if cv2.waitKey(100) == ord('q'): # Termina cuando se apriete q
                break
        else:
            video.release()
            break
    cv2.destroyAllWindows()

detectMovement()