# Using agents to do FileMaker development work

To work on a FileMaker file an agent can use one of two methods to connect to the file:

1. Backdoor method: use the **Claris ADT harness to directly read and manipulate shared FileMaker files**

   - either files hosted on a FileMaker Server
   - or local files shared using peer-to-peer networking, with Multiuser turned on.

2. Frontdoor method: use **fmIDE to work directly within the FileMaker Client GUI on any open file**

   - either using the **fmIDE 'Name that Thing' API** to navigate to and open the relevant FileMaker development context for the object being worked on.
   - or using the **fmIDE Action Script API** to perform a sequence of FileMaker development actions.

These two methods are complementary, not exclusive:

- The backdoor method is for when the agent is working in **'standalone mode'**, without a developer present.
  - The agent can work directly in the FileMaker file, without needing to open the FileMaker GUI.
- The frontdoor method is for when the agent is working with the developer in **'companion mode'** with the developer together.
  - The agent can show stuff and take action within the GUI.

## Using agents on standalone local files / Turning Multi-User Mode On and Off

When working with standalone, local files - non-shred files like fmWorkMate - the two aaproaches can be combined to help turn Multiuser mode on and off as needed:

1. When a file is open in the FileMaker GUI and supports fmIDE v0.87 or higher, the agent can use the **fmIDE Action `[+].Set Multi-User = 1`** to turn Multi-User (peer-to-peer sharing) on.
2. Then the agent can also use the **backdoor method** to work directly on the file, as needed.
3. When the file is ready for release the agent can turn Multi-User off again, either via the DT or using the **fmIDE Action `[+].Set Multi-User = 0`**


This is particularly useful when developing **local tools which are intended to work offline**. 

The development workflow can therefore begin very simply:

- Open the file
- Turn Multi-User On
- Start working with the agent

The complete lifecycle becomes:

- User prompts agent
- Agent opens local file
- Agent enables Multi-User using fmIDE
- Agent-assisted development using Claris ADT and/or fmIDE
- Agent performs release process
  - disables Multi-User
  - performs release of offline file
