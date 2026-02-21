# FTP Log Poisoning

xpl0ited by [infrar3d](https://github.com/Infrar3dd)

**FTP Log Poisoning** is a vulnerability which works in tandem with **LFI**

It works if text from LFI was read like a PHP code.

```bash
python3 ftp_log_poisoning.py --help
usage: ftp_log_poisoning.py [-h] -u URL -p PORT -c COMMAND [--shell] [-l LPORT]

FTP Log Poisoning exploit

options:
  -h, --help            show this help message and exit
  -u, --url URL         Target URL
  -p, --port PORT       FTP port
  -c, --command COMMAND
                        Command to execute
  --shell               Open shell
  -l, --lport LPORT     Listen port

```
Example:

![](https://github.com/Industri4l-H3ll-Xpl0it3rs/FTP-Log-Poisoning/blob/main/Example.jpg)

### ⚠️ Disclaimer ⚠️

This software and proof-of-concept code is provided **for educational and research purposes only**. 

*   The authors are **not responsible** for any misuse or damage caused by this program.
*   **Do not use** against any systems without explicit **prior permission**.
*   Use of this tools for attacking targets without consent is **illegal**.

You are responsible for obeying all applicable laws. **Use ethically and responsibly.**
