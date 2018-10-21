# SLCBInternationalHello

A Streamlabs Chatbot script that will reply configure your bot to say hello to users saying hello.

## How to Import into Streamlabs Chatbot
* Streamlabs Chatbot supports importing scripts as Zip files.
* To download the `SLCBInternationalHello` Zip file:
    * Find all the releases by going to [releases tab](https://github.com/sktse/SLCBInternationalHello/releases)
    * For the version you want to use, click the `Source code (zip)` link to get the Zip file.

![Streamlabs Chatbot Screenshot](https://user-images.githubusercontent.com/11049883/47262578-37349a80-d4ba-11e8-9812-c3354bebc13d.png)
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Import button ![import button](https://user-images.githubusercontent.com/11049883/47262592-be820e00-d4ba-11e8-9dae-38d84aa4c774.png) in the top right corner of the tab.
* This will open up a file explorer.  Select the downloaded Zip file.

## How to Configure the Script
### Permission
* The Permission dropdown uses the standard Streamlab Chatbot permission levels.
* The possible options are:
    * `everyone`
    * `moderator`
    * `subscriber`
    * `user_specific`
    * `editor`

### Info
* The Info textbox is for when Permission is set to `user_specific`.
* Enter the user name that you specifically want to have access to this script.

### Cooldown
* The Cooldown slider is to set the duration between replies to a specific user.
* The Cooldown is set to a long period of time to stop the Chatbot from spamming the channel when _other_ people reply to a user initally greeting the chat.

### Enable Logging
* The Enable Logging checkbox turns on very aggressive logging for this script.
* Use to help develop and debug this script.
* It is _not recommended_ you leave this on because it will make your log files large.
