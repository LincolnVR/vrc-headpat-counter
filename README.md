# VRChat Headpat+ Counter

### <b>[How To Setup](#How-To-Setup) | [Customize Your Parameters](#Customize-Your-Parameters) | [See It In Action](#See-It-In-Action)</b><br><br>

## <b>What is this? </b><br>

### <b><i>A dynamic counter for VRChat. This script uses parameters setup inside VRC Contact Receivers. It will track and temporarily display set properties into VRC's chatbox each time one of those properties is incremented.</b></i>

<br>

## <b>How To Setup</b>

> ### <b>[Unity Setup](#Unity-Setup) -> [OCS Parameters Setup](#OSC-Parameters-Setup) -> [Launching This Program](#Launching-Program)</b>

<br>

## <a name="Unity-Setup"></a><b>Unit Setup</b>

---

    1. Add a `VRC Contact Receiver` component to your avatar.
    2. Checkmark `Allow Others` inside the `VRC Contact Receiver`
    3. Set the Parameter you would like to track in the `Parameter` field of `VRC Contact Receiver`. This must be named with a `Track_` before the parameter name in order to work with this script (see example below).
    4. Add which collisions you want to trigger the increment of the parameter inside the `VRC Contact Receiver`.

### Example of adding Headpats as a Parameter:

![Example Image](docs/images/Unity_Example.png)

> Note: that in the above example the collider has been attached to my head and the `Track_Headpats` parameter will only triger when a `Hand`, `HandL`, or `HandR` enter that collider.<br>
> You can [Add any parameter](#Customize-Your-Parameters) that you want. It does not need to be headpats. See the example [Steppies setup](#Customize-Your-Parameters)

<br>

## <a name="OSC-Parameters-Setup"></a><b>OSC Parameters Setup</b>

---

Your avatar will need the put your new parameters into your VRC OSC file. The file can be found in a path such as `C:\Users\your_user_name\AppData\LocalLow\VRChat\VRChat\OSC\your_user_id\Avatars` Each avatar has automatically created files for OSC parameters when it is first loaded. The files are named using that avatars ID. If this is not your first time building the avatar you will either need to:

> ## Do <b>ONE</b> of the two:

### <b>Option 1 -></b> Manually add the parameters in the avatars OSC file.

### <b>Option 2 -></b> Delete the OSC file associated with that avatar so that it will automatically generate a new one when you next load your avatar in game.

<br>

> Note: you can find your avatars ID inside the `Pipeline Manager(Script)` component in Unity.
> ![Avatar ID](docs/images/VRC_Avatar_Descriptor.png)

### Example of maunally adding the Headpats parameter:

![Avatar ID](docs/images/Edit_OSC_JSON.png)

<br>

## <a name="Launching-Program"></a><b>Launching This Program</b>

---

- ## [Download Python](https://www.python.org/downloads/)
- ## Download this Github Repo as Zip
- ## Extract Zip
- ## Run `launch.bat`

<br>

## <a name="Customize-Your-Parameters"></a><b>Customize Your Parameters</b>

---

This script is not limited to Headpats or just one parameter at a time! You can have multiple trackers setup at once. In the ["See It In Action"](#See-It-In-Action) section I have both `Headpats`, and `Steppies` setup on my avatar. You can easily add many more. The only limitation would come from the character limit inside VRC's chatbox.

Each Parameter will need its own `VRC Contact Receiver` and remember to name each parameter starting with `Track_`. So for steppies it is `Track_Steppies`.

> ### Example Setup of Steppies Counter:
>
> ![Avatar ID](docs/images/Track_Steppies.png) > <br>
> In this example I have named my parameter `Track_Steppies` and have set the collision to react to `Foot`, `FootR`, and `FootL`

<br>

## <a name="See-It-In-Action"></a><b>See It In Action</b>

---

![Headpats](docs/gifs/Headpats.gif)
![Steppies](docs/gifs/Steppies.gif)
