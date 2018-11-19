# Releases

## v1.2.0 - Porchetta
* Link: [v1.2.0 - Porchetta]()
* Adds the ability to add custom output greetings.
    * Custom output greetings are set with a semi-colon separated string.
    * Each greeting can be multiple words.
    * The percentage occurrence of the custom of greetings is set with a slider from 0% to 100%.
* Adds greetings in Estonian, Igbo, Yoruba, and American.
* Adds support to trigger the custom greeting when the last character in the command is a punctuation.
* Adds clarification to Streamlabs Chatbot Python installation.
* Adds developer hygiene things
    * Adds unit tests! Yay!
    * Adds continuous integration! Continuously Yay!
    * Adds automatic builds!
    * Adds Makefiles for all these things!

## v1.1.0 - Ceviche
* Link: [v1.1.0 - Ceviche](https://github.com/sktse/SLCBInternationalHello/releases/tag/v1.1.0)
* Adds the ability to add custom input commands to trigger a greeting response.
    * Custom input commands are set with a semi-colon separated string.
    * Each custom command can only be one word.
    * This is because the script currently only checks the first word of every message.
* Added "Hey" as a standard set of greetings.
* Added more installation details in the README.
* Increased logging.

## v1.0.1 - Kielbasa
* Link: [v1.0.1 - Kielbasa](https://github.com/sktse/SLCBInternationalHello/releases/tag/v1.0.1)
* Fixes non-latin greetings with Unicode encoding.
* Increases the "randomness" of greeting selection.
* Adds some more greetings.
* Increases cooldown to 240 minutes (4 hours).
* Removes unused settings properties. They got overwritten and wiped out anyway.

## v1.0.0 - Kimchi
* Link: [v1.0.0 - Kimchi](https://github.com/sktse/SLCBInternationalHello/releases/tag/v1.0.0)
* The initial release of the script!
* Whenever a user says something in chat, If it is in the list of greetings, the bot will reply with a greeting at the user.
* The settings configuration allows for:
    * Permission --> Which uses standard StreamLabs Chat Bot permissions
    * Info --> Which is for specific users permissions (standard StreamLabs Chat Bot permissions)
    * Cooldown time (Minutes) --> The cooldown for how long the bot will reply.
        * Used to stop the bot from replying to other people saying hello to other users.
        * Presumably, someone says hello when they initially come into chat.  So we can have cooldown periods of 1 hour
        * Enable Debugging --> Turns on super aggressive logging for everything.
