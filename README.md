# Eye Blinking
This module is deeply centered around predicting the facial landmarks of the given face in a video. We can accomplish a lot of things using these landmarks. From detecting eye-blinks in a video to predicting emotions of the subject. The applications, outcomes and possibilities of facial landmarks are immense and intriguing.

Dlib's prebuilt model, which is essentially an implementation of, not only does a fast face-detection but also allows us to accurately predict 68 2D facial landmarks. Very handy. Also Adrian Rosebrock's imutils package was super helpful, checkout his tutorials at.

![facial-landmarks-68](https://user-images.githubusercontent.com/47856985/158023361-871b70d4-1068-4a26-85d2-4606ab45b249.jpg)

Using these predicted landmarks of the face, we can build appropriate features that will further allow us to detect certain actions, like using the eye-aspect-ratio (more on this below) to detect a blink or a wink. In this project, these actions are programmed as triggers the inputs - "dits" and "dahs".
Eye-Aspect-Ratio (EAR)

![EAR-final](https://user-images.githubusercontent.com/47856985/158023366-4c543d5c-6cb1-4d8b-af93-c9a8e5788d41.png)


You will see that Eye-Aspect-Ratio is the simplest and the most elegant feature that takes good advantage of the facial landmarks. EAR helps us in detecting blinks and winks etc.

You can see that the EAR value drops whenever the eye closes. We can train a simple classifier to detect the drop. However, a normal if condition works just fine.
