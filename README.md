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

## Supported Greetings
* This script currently will reply with the following greetings:

| Greeting | Pronouncation | Language |
| --- | --- | --- |
| Hello | | English |
| Greetings | | English |
| Hi | | English
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

