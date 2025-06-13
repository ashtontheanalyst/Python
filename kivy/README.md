# Kivy App Development
Kivy is a python library that allows you to develop applications for cross platform use. Instead of
having to learn multiple languages and devices, you can make your app in python and then deploy it
on any device including Android, iOS, Windows, Linux, etc.

![Alt Text](./assets/kivy.png)

## Learning
In order to get more familiar with this library, I am following the official [documentation](https://kivy.org/doc/stable/guide/basic.html#quickstart) stack!
- [`pong/`](/pong/) is a fully built game of pong based on the documentation
- [`basic.py`](./basic.py) is a simple app that opens a black window and shows text.
- [`login.py`](./login.py) is an app with a grid for username and password, no actual functionality though.

## ATAK Clone Development
- Ref: https://www.youtube.com/watch?v=6gNpSuE01qE&t=624s
- Create a PoC application, use the pong one maybe
- Get a VM running with some linux flavor
- Download the app onto the linux box
- Compile it with **BUILDOZER** so that we get a working `APK`
- Create a VM with some flavor of Android
- Download the APK onto the Android VM, use the application
- From there we have proof of using an application I developed on an Android device, time for ATAK...

## Notes
- For VS Code, there's an extenstion called `Kivy` that will help with syntax highlighting and fill