
# AnonCTF_2019: Ram into me

**Category:** Forensics
**Points:** 20

**Problem Statement:**
><P>Asta was behaving weird quite lately and used to stick into his computer all day-in and out.Yuno is an excellent hacker and being a good friend of Asta worried for him.He took the ram-dump of Asta's computer to find out what he's been doing in his computer?<BR>Can you help Yuno find, what is in the ram-dump?</P>

><A href="https://drive.google.com/drive/folders/1hLNtA_XvuAaERG3m6RpuoodILEBFJEbs?usp=sharing">RAM DUMP</A>

## Write-Up
Download the file <B>memdump.mem</B>.<BR>
There's a tool called volatility which can analyze the memory dump.<BR>
You can run the following command for more info.
><P>$ volatility -h</P>

<h4>STEP 1</h4>

> First lets analyze on  what type of system, image has been taken<BR>
   
   ![Attached Image](Capture.PNG)


<P>It shows profile as <B>WinXPSP2x86</B> , keep that in mind</P>

<h4>STEP 2</h4>

> Lets see what are the running processes in the system
  
   ![Attached Image](Capture2.PNG)
 
<P>There are no suspicious processes running except <B>IEXPLORE.EXE</B> having process id 1340 and 1396</P>
 
<h4>STEP 3</h4>
 
 >We'll check the history of internet explorer
 
   ![Attached Image](Capture3.PNG)
 
   ![Attached Image](Capture4.PNG)
  
 
<h4>STEP 4</h4>
 
 >lets visit the site and see whats there
 
   ![Attached Image](Capture5.PNG)

There's the flag we want <B>anonCTF{MY-m3m0ry_1$_w3@k}</B>
