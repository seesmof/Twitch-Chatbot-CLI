### Plans for rebuilding the app and adding GUI

The application we're planning to build involves several components, including a chatbot and various features. The chatbot will be authenticated using a key obtained from a specific website. This key needs to be stored securely and accessed throughout the app. For this purpose, we'll create a `.env` file in a dedicated data folder. This approach allows us to use environmental variables to store sensitive data securely.

We also need to consider the user interface. To ensure the app cannot be started without a key, we need to implement an authentication mechanism. Additionally, we need to provide a username for our bot account.

To facilitate these functionalities, we propose the creation of a settings page. On this page, users can enter the bot's name, key, and manage channels. Each channel management feature includes fields for adding or removing channels and corresponding buttons for these actions. Below this, we'll display a list of currently active channels.

The main features of our application include memory, logging, delay between messages, and persona. The delay between messages feature, if enabled, will show an input field for setting the delay. The persona feature will present a list of personas, and upon double-clicking on any of them, we'll open a new window displaying the persona's details, including name, prompt, and modification capabilities. However, this task is complex and will initially be marked as optional.

Here is a formal representation of our planned structure:

- **Home Page**
  - Chat
- **Bot Settings**
  - Set username
  - Set key
  - Set channels
- **Features settings**
  - Memory
  - Logging
  - Delay between messages
    - If on, shows an input field to set the delay between messages
  - Persona
    - Toggle on/off
    - When on, displays a list of personas. Upon double-clicking on any persona, opens a new window with the persona's info (name, prompt, and ability to modify data). This feature is optional.
