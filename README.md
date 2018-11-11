# SLCBInternationalHello

[![Latest](https://img.shields.io/github/release/sktse/SLCBInternationalHello.svg)](https://github.com/sktse/SLCBInternationalHello/releases/latest/) 
[![CircleCI](https://circleci.com/gh/sktse/SLCBInternationalHello/tree/master.svg?style=svg)](https://circleci.com/gh/sktse/SLCBInternationalHello/tree/master)

* A Streamlabs Chatbot script that will reply configure your bot to say hello to users saying hello.
* Download the latest version (v1.1.0) of the script [here](https://github.com/sktse/SLCBInternationalHello/releases/download/v1.1.0/SLCBInternationalHello.zip).

### Table of Contents
* [Details](#details)
* [Installation](#installation)
    * [Installing Python 2.7.13](#install_python)
    * [Configuring Python for Streamlabs Chatbot](#configure_python)
    * [Importing Scripts into Streamlabs Chatbot](#import_script)
    * [Manually Uninstalling Scripts from Streamlabs Chatbot](#uninstall)
* [Configuring the International Hello Script](#configuration)
    * [Permission](#configuration_permission)
    * [Info](#configuration_info)
    * [Cooldown](#configuration_cooldown)
    * [Enable Custom Commands](#configuration_enable_commands)
    * [Custom Commands](#configuration_commands)
    * [Enable Logging](#configuration_logging)
* [Supported Greetings](#greetings)
* [For Developers](#for-developers)

<a name="details"/>

## Details
![Hello to you too](https://user-images.githubusercontent.com/11049883/47270459-190e7f00-d53a-11e8-8cc3-7029db9daf27.png)

* Whenever a user starts a chat message with any of the greetings below, the bot will randomly say a greeting back at the user.
* The cooldown per user can be configured for a long duration (up to 4 hours).
* This prevents your Chatbot from saying hello to people who were replying to someone else.

<a name="installation"/>

## Installation

<a name="install_python"/>

### Installing Python 2.7.13
* Streamlabs Chatbot scripts require that you have Python 2.7.13 installed on your local machine.
* You can download Python 2.7.13 from the official [Python Software Foundation Download page](https://www.python.org/downloads/release/python-2713/).
    * This is the direct link to the [Windows x86-64 MSI installer](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi).
* Run the `msi` file to install Python 2.7.13. You can do this by double-clicking the file.
* Go through the Python 2.7.13 installer wizard.
* By default, the installer will save Python in `C:\Python27`

<a name="configure_python"/>

### Configuring Python for Streamlabs Chatbot
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Settings button ![settings button](https://user-images.githubusercontent.com/11049883/47404591-eae89500-d71b-11e8-8a4e-89b3902a2541.png) in the top right corner of the tab.

![global script settings](https://user-images.githubusercontent.com/11049883/47404567-d1dfe400-d71b-11e8-9628-c76fe6942bc4.png)
* This will open up the Global Scrip Settings page for Streamlabs Chatbot
* Click the **Pick Folder** under the **Python 2.7.13 Directory** section
* This will open up a file explorer.  Select the folder of `\Python27\lib` folder.
    * The default Python installation path is `C:\Python27\lib`

<a name="import_script"/>

### Importing Scripts into Streamlabs Chatbot
* Streamlabs Chatbot supports importing scripts as Zip files.
* To download the `SLCBInternationalHello` Zip file:
    * Find the latest release by go to the [latest release page](https://github.com/sktse/SLCBInternationalHello/releases/latest)
    * Find all the releases, including older versions, by going to [releases tab](https://github.com/sktse/SLCBInternationalHello/releases)
    * For the version you want to use, click the ![SLCBInternationalHello.zip](https://user-images.githubusercontent.com/11049883/47473761-fbfbd980-d7e1-11e8-874d-276b50d835b6.png) link to download the Streamlabs Chatbot compatible Zip file.

![Streamlabs Chatbot Screenshot](https://user-images.githubusercontent.com/11049883/47262578-37349a80-d4ba-11e8-9812-c3354bebc13d.png)
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Import button ![import button](https://user-images.githubusercontent.com/11049883/47262592-be820e00-d4ba-11e8-9dae-38d84aa4c774.png) in the top right corner of the tab.
* This will open up a file explorer.  Select the downloaded Zip file.

<a name="uninstall"/>

### Manually Uninstalling Scripts from Streamlabs Chatbot
* In your File Explorer, go to the folder where Streamlabs Chatbot is installed.
    * By default, Streamlabs Chatbot will be installed in `C:\Users\<your user name>\AppData\Roaming\Streamlabs\Streamlabs Chatbot`
* From the Streamlabs Chatbot folder, go to `\Services\Scripts`.  This is where Streamlabs Chatbot installs all the scripts.
* Delete any folders that start with `SLCBInternationalHello`.
* In the Streamlabs Chatbot Scripts panel, click the Reload button ![refresh button](https://user-images.githubusercontent.com/11049883/47473935-ce636000-d7e2-11e8-89b6-86fed4c6c92c.png) to upload your scripts.
* The International Hello script should now be removed. 

<a name="configuration"/>

## Configuring the International Hello Script

![script settings](https://user-images.githubusercontent.com/11049883/47404903-30599200-d71d-11e8-8f77-e14362160144.png)

* Click the name of the script to open up the configuration panel on the left side of Streamlabs Chatbot.
* When you make _any_ settings changes, you _must_ click the `Save Settings` button.
    * Only when the `Save Settings` button is pressed with the settings take affect.

<a name="configuration_permission"/>

### Permission
* The Permission dropdown uses the standard Streamlab Chatbot permission levels.
* The possible options are:
    * `everyone`
    * `moderator`
    * `subscriber`
    * `user_specific`
    * `editor`

<a name="configuration_info"/>

### Info
* The Info textbox is for when Permission is set to `user_specific`.
* Enter the user name that you specifically want to have access to this script.

<a name="configuration_cooldown"/>

### Cooldown
* The Cooldown slider is to set the duration between replies to a specific user.
* The Cooldown is set to a long period of time to stop the Chatbot from spamming the channel when _other_ people reply to a user initally greeting the chat.

<a name="configuration_enable_commands"/>

### Enable Custom Commands
* The Enable Custom Commands checkbox turns on custom input commands in the **Custom Commands** section.
* Enable this feature if you want the script to be triggered by your own custom commands.

<a name="configuration_commands"/>

### Custom Commands
* The Custom Commands textox is for when Enable Custom Commands checkbox is turned on.
* Enter your own custom input commands that will trigger a greeting response.
* Your custom input commands must:
    * Be a single word
    * Be semi-colon separated for multiple custom commands
* Example: When you enter `!hello;banana;heyo!`, when a user enters `!hello`, `banana`, or `heyo!` into chat, the script will reply with a greeting.

<a name="configuration_logging"/>

### Enable Logging
* The Enable Logging checkbox turns on very aggressive logging for this script.
* Enable this to help the development and debugging the script.
* It is _not recommended_ you leave this on because it will make your log files large.

<a name="greetings"/>

## Supported Greetings
* This script currently will reply with the following greetings:

| Greeting | Pronouncation | Language |
| --- | --- | --- |
| Hello | | English |
| Greetings | | English |
| Hi | | English |
| Hey | | English |
| Allo | | French |
| Bonjour | | French |
| Top-o-the-morning | | English |
| Hola | | Spanish |
| Ciao | | Italian |
| Buongiorno | | Italian |
| Hallo | | German |
| Guten tag | | German |
| Moin moin | | German |
| Namaste | | Hindi |
| Salaam | | Farsi |
| Merhaba | | Turkish |
| Szia | | Hungarian |
| Hej | | Swedish, Danish |
| Zdravo | | Croatian |
| Ahoj | | Czech |
| Kamusta | | Flipino |
| Hei | | Finnish, Norwegian |
| God dag | | Norwegian |
| Halo | | Indonesian |
| Sveiki | | Latvian |
| Salut | | Romanian, etc |
| Ahoj | | Slovak |
| Sawubona | | Zulu |
| Hullo | | Scottish |
| Dia dhuit | | Gaelic |
| G'day | | Australian |
| Aloha | | Hawaiian |
| Tere | | Estonian |
| Howdy | | American |
| xin ch&#xe0;o | | Vietnamese |
| Dzie&#x0144; dobry | | Polish |
| Ol&#xe1; | | Portugese |
| &#x0e2a;&#x0e27;&#x0e31;&#x0e2a;&#x0e14;&#x0e35; | swasdi | Thai |
| &#x3053;&#x3093;&#x306b;&#x3061;&#x306f; | Kon'nichiwa  | Japanese |
| &#x3082;&#x3057;&#x3082;&#x3057; | Moshi Moshi | Japanese |
| &#xc5ec;&#xbcf4;&#xc138;&#xc694; | yeoboseyo | Korean |
| &#x0421;&#x0430;&#x0439;&#x043d; &#x0443;&#x0443; | Sain uu | Mongolian |
| &#x0421;&#x04d9;&#x043b;&#x0435;&#x043c;&#x0435;&#x0442;&#x0441;&#x0456;&#x0437; &#x0431;&#x0435; | Salemetsiz be | Kazakh |
| &#x041f;&#x0440;&#x0438;&#x0432;&#x0435;&#x0442; | Privet | Russian  |
| &#x4f60;&#x597d; | Ni Hao | Chinese |
| P&#xeb;rsh&#xeb;ndetje | | Albanian |
| &#x1230;&#x120b;&#x121d; | selami | Amharic |
| &#x0645;&#x0631;&#x062d;&#x0628;&#x0627; | marhabaan | Arabic |
| &#x03b3;&#x03b5;&#x03b9;&#x03b1; &#x03c3;&#x03b1;&#x03c2; | geia sas | Greek |

<a name="for-developers"/>

## For Developers

* To setup the project, run `make install`
* To run tests, run `make test`
* To build the Streamlabs Chatbot `zip` file for release, run `make release`
* To reset the environment, run `make clean`
