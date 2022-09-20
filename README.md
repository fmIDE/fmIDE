![fmIDE Logo][fmIDE]
# fmIDE
A FileMaker Integrated Development Environment

Made [by FileMaker Developers][MrWatson.de] for FileMaker Developers.

fmIDE is

- A FileMaker module to make integration of your FileMaker database into your development processes and analysis tools easier and tighter!
- A single script API
- A vision!

---

Official launch coming at the [fmGuru conference][] Sat. 8th October 2022

"give wings to your FileMaker Development"


[![Rome FileMaker Week](https://www.mettilealialtuosviluppofilemaker.com/wp-content/uploads/2022/06/Sorgente_Logo_Rome-Filemaker-week-768x298.png)][fmGuru conference]

Watch this Space for more!

---

## Installing fmIDE

1. Download
   - Download and open the fmIDE file in FileMaker
2. Copy
   - Open the Script Workspace
   - Copy the `fmIDE Module` folder (or just the `fmIDE` script, if you want a minimal footprint) 
3. Paste & Permit
   - In each database file of your solution
     1. Paste the code into the Script Workspace
     2. Grant your [FullAccess] users permission to use the fmp url in each solution file
       - Open `Security > Advanced > Extended Privileges` 
       - choose the `fmurlscript` extended privilege
       - check the [FullAccess] privilige set

## Hello from fmIDE

If you have the fmIDE file open in FileMaker, try this:

[Run the `Hello` script](fmp://$/fmIDE?script=Hello) in the fmIDE demo file (to test fmp-url permissions):

    fmp://$/fmIDE?script=Hello

[Edit the `Hello` script](fmp://$/fmIDE?script=fmIDE&$script_name=Hello) using the `fmIDE 'name that thing' API`:

    fmp://$/fmIDE?script=fmIDE&$script_name=Hello


Note: fmp-urls are sadly not supported in GitHub
- For now, to follow the fmp url please copy+paste the urls to your browser's address line.
- Maybe later, we can get a project started to create a Chrome extension to add links to fmp urls?


---

[fmIDE]:https://github.com/fmIDE/fmIDE/wiki/images/fmIDE.png
[fmIDE Integrate]:docs/fmIDE_Integrate.png
[fmIDE Logo]:docs/fmIDE_Logo.png
[fmGuru conference]:https://www.mettilealialtuosviluppofilemaker.com/en/
[MrWatson.de]:http://www.mrwatson.de