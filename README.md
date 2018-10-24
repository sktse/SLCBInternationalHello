# SLCBInternationalHello

A Streamlabs Chatbot script that will reply configure your bot to say hello to users saying hello.

### Table of Contents
* [Details](#details)
* [Installation](#installation)
    * [Installing Python 2.7.13](#install_python)
    * [Setting Python for Streamlabs Chatbot](#configure_python)
    * [How to Import into Streamlabs Chatbot](#import_script)
* [How to Configure the Script](#configuration)
    * [Permission](#configuration_permission)
    * [Info](#configuration_info)
    * [Cooldown](#configuration_cooldown)
    * [Enable Custom Commands](#configuration_enable_commands)
    * [Custom Commands](#configuration_commands)
    * [Enable Logging](#configuration_logging)
* [Supported Greetings](#greetings)

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
* By default, the installer will save Python in `C:\Python27`

<a name="configure_python"/>

### Setting Python for Streamlabs Chatbot
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Settings button ![settings button](https://user-images.githubusercontent.com/11049883/47404591-eae89500-d71b-11e8-8a4e-89b3902a2541.png) in the top right corner of the tab.

![global script settings](https://user-images.githubusercontent.com/11049883/47404567-d1dfe400-d71b-11e8-9628-c76fe6942bc4.png)
* This will open up the Global Scrip Settings page for Streamlabs Chatbot
* Click the **Pick Folder** under the **Python 2.7.13 Directory** section
* This will open up a file explorer.  Select the folder of `\Python27\lib` folder.
    * The default Python installation path is `C:\Python27\lib`

<a name="import_script"/>

### How to Import into Streamlabs Chatbot
* Streamlabs Chatbot supports importing scripts as Zip files.
* To download the `SLCBInternationalHello` Zip file:
    * Find all the releases by going to [releases tab](https://github.com/sktse/SLCBInternationalHello/releases)
    * For the version you want to use, click the ![Source code (zip)](https://user-images.githubusercontent.com/11049883/47276930-ee97e280-d588-11e8-870c-b6892fcaefe1.png) link to get the Zip file.

![Streamlabs Chatbot Screenshot](https://user-images.githubusercontent.com/11049883/47262578-37349a80-d4ba-11e8-9812-c3354bebc13d.png)
* In Streamlabs Chatbot, select the Scripts tab on the left menu.
* Select the Import button ![import button](https://user-images.githubusercontent.com/11049883/47262592-be820e00-d4ba-11e8-9dae-38d84aa4c774.png) in the top right corner of the tab.
* This will open up a file explorer.  Select the downloaded Zip file.

<a name="configuration"/>

## How to Configure the Script

![script settings](https://user-images.githubusercontent.com/11049883/47404903-30599200-d71d-11e8-8f77-e14362160144.png)

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

