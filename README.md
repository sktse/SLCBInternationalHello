# SLCBInternationalHello

[![Latest](https://img.shields.io/github/release/sktse/SLCBInternationalHello.svg)](https://github.com/sktse/SLCBInternationalHello/releases/latest/) 
[![CircleCI](https://circleci.com/gh/sktse/SLCBInternationalHello/tree/master.svg?style=svg)](https://circleci.com/gh/sktse/SLCBInternationalHello/tree/master)

* A Streamlabs Chatbot script that will reply configure your bot to say hello to users saying hello.
* Download the latest version (v1.2.0) of the script [here](https://github.com/sktse/SLCBInternationalHello/releases/download/v1.2.0/SLCBInternationalHello.zip).

### Table of Contents
* [Details](#details)
* [Installation](#installation)
    * [Installing Python 2.7.13](#install_python)
    * [Configuring Python for Streamlabs Chatbot](#configure_python)
    * [Importing Scripts into Streamlabs Chatbot](#import_script)
    * [Manually Uninstalling Scripts from Streamlabs Chatbot](#uninstall)
* [Configuring the International Hello Script](#configuration)
    * [Core Settings Group](#configuration_group_core)
        * [Permission](#configuration_permission)
        * [Info](#configuration_info)
        * [Cooldown](#configuration_cooldown)
    * [Customization Settings Group](#configuration_group_customization)
        * [Enable Custom Commands](#configuration_enable_commands)
        * [Custom Commands](#configuration_commands)
        * [Enable Custom Outputs](#configuration_enable_outputs)
        * [Custom Output Percentage](#configuration_output_percentage)
        * [Custom Outputs](#configuration_output_greetings)
    * [Developer Settings Group](#configuration_group_developer)
        * [Enable Logging](#configuration_logging)
* [Supported Greetings](#greetings)
* [For Developers](#for-developers)
    * [Running the Script](#running-script)
        * [For Windows Systems](#running-script-windows)
        * [For Non-Windows Systems](#running-script-linux)

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
* Select the Import button ![import button](https://user-images.githubusercontent.com/11049883/48686710-71618c80-eb8b-11e8-838c-4bf83bde9438.png) in the top right corner of the tab.
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

* Click the name of the script to open up the configuration panel on the left side of Streamlabs Chatbot.
* When you make _any_ settings changes, you _must_ click the `Save Settings` button.
    * Only when the `Save Settings` button is pressed with the settings take affect.

<a name="configuration_group_core"/>

### Core Settings Group

![Core settings group](https://user-images.githubusercontent.com/11049883/50360566-6dc87900-052e-11e9-83ab-9141a86911d4.png)

* The Core settings group contains the basic operational configurations for the script.

<a name="open_readme"/>

### Open README

* Opens the README file for this script.
* The README file is an HTML version of this document - `README.md`

<a name="configuration_permission"/>

#### Permission
* The Permission dropdown uses the standard Streamlab Chatbot permission levels.
* The possible options are:
    * `everyone`
    * `moderator`
    * `subscriber`
    * `user_specific`
    * `editor`

<a name="configuration_info"/>

#### Info
* The Info textbox is for when Permission is set to `user_specific`.
* Enter the user name that you specifically want to have access to this script.

<a name="configuration_cooldown"/>

#### Cooldown
* The Cooldown slider is to set the duration between replies to a specific user.
* The Cooldown is set to a long period of time to stop the Chatbot from spamming the channel when _other_ people reply to a user initially greeting the chat.

<a name="configuration_group_customization"/>

### Customization Settings Group

![Customization settings group](https://user-images.githubusercontent.com/11049883/48686970-fdc07f00-eb8c-11e8-804b-baf84b5f2ef8.png)

* The Customization settings group contains the configuration that allow you to personalize the scripts behaviour.

<a name="configuration_enable_commands"/>

#### Enable Custom Commands
* The Enable Custom Commands checkbox turns on custom input commands in the **Custom Commands** section.
* Enable this feature if you want the script to be triggered by your own custom commands.

<a name="configuration_commands"/>

#### Custom Commands
* The Custom Commands textbox is for when **Enable Custom Commands** checkbox is turned on.
* Enter your own custom input commands that will trigger a greeting response.
* Your custom input commands must:
    * Be a single word
    * Be semi-colon separated for multiple custom commands
* Example: When you enter `!hello;banana;heyo!`, when a user enters `!hello`, `banana`, or `heyo!` into chat, the script will reply with a greeting.

<a name="configuration_enable_outputs"/>

#### Enable Custom Outputs
* The Enable Custom Outputs checkbox turns on custom output greetings in the **Custom Outputs** section.
* Enable this feature if you want the script to reply with your own custom greetings whenever a user says hello.

<a name="configuration_output_percentage" />

#### Custom Output Percentage
* The Custom Output Percentage slider is for when **Enabled Custom Outputs** checkbox is turned on.
* Set the value to the percentage of replies you want to be picked from your pool of custom greetings.
* The values range from 0% (i.e. never picking from your pool of custom greetings) to 100% (i.e. always picking from your pool of custom greetings).

<a name="configuration_output_greetings" />

#### Custom Outputs
* The Custom Outputs textbox is for when **Enabled Custom Outputs** checkbox is turned on.
* Enter your own custom output greetings that will be sent to the user whenever the user triggers a greeting.
* Your custom output commands must:
     * Be sem-colon separated for multiple custom commands
     * Can be multiple words
* Example: When you enter `You had me at hello;Say hello to my little friend;Live long and prosper`, the pool of custom output greetings are:
    * `You had me at hello`
    * `Say hello to my little friend`
    * `Live long and prosper`
* When a custom greeting is triggered, it will randomly select one from the custom greetings pool. 

<a name="configuration_group_developer"/>

### Developer Settings Group

![Developer settings group](https://user-images.githubusercontent.com/11049883/48687635-462d6c00-eb90-11e8-8bde-109d2125e432.png)

* The Developer settings group contains the configurations for developers to debug the script. Please only use if you are an expert!

<a name="configuration_logging"/>

#### Enable Logging
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
| Ked&#x1EE5; | | Igbo |
| Bawo ni | | Yoruba |

<a name="for-developers"/>

## For Developers

* To setup the project, run `make install`
    * For Windows development environments, you can run `make install-win` to additionally install the .NET dependencies.
* To run tests, run `make test`
* To build the Streamlabs Chatbot `zip` file for release, run `make release`
* To reset the environment, run `make clean`

<a name="running-script"/>

### Running the Script

* Streamlabs ChatBot is a .Net application that uses the `pythonnet` module to integrate with Python.
* This shows up in the script as `import clr`.

<a name="running-script-windows"/>

#### For Windows Systems
* Run `make install-win` to install the `pythonnet` module.
* You should be able to directly run the script now.
    * This is currently untested. Please provide feedback!

<a name="running-script-linux"/>

#### For Non-Windows Systems
* A way to get `pythonnet` to install properly in the virtual environment has not bee found.
    * The instructions provided by `pythonnet` [here](https://github.com/pythonnet/pythonnet/wiki/Troubleshooting-on-Windows,-Linux,-and-OSX#installation-instructions-for-homebrew-cask-mono-mdk) have not worked.
* Testing is limited to "testing on prod" by installing the script in Streamlabs ChatBot.
* If you do not have access to the CircleCI artifacts, you can manually build the release zip file.
* Run `make release` to build the zip file.
* Import it via the [Importing Scripts into Streamlabs Chatbot](#import_script) 
