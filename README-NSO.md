# Nintendo Switch Online App mitmproxy

1. Install mitmproxy

2. Create mitmproxy Android Virtual Device (AVD)

3. Install Nintendo Switch Online App

4. Launch `mitmproxy`

- If we use wireshark too, then set a `SSLKEYLOGFILE`

```bash
SSLKEYLOGFILE="./sslkeylogfile.txt" ./mitmproxy
```

5. Set AVD proxy

- Click dot-dot-dot

- Setting proxy to mitmproxy (127.0.0.1:8080)

6. Do some surf to mitmproxy

- If we use wireshark too, Set a `Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename`

7. Save pcap and mitmproxy

- In `mitmproxy`, Type `w`

- In `wireshark`, `File-Save`

# References

- [Nintendo Switch Online App Cookie Reverse-Engineering](https://github.com/frozenpandaman/splatnet2statink/wiki/mitmproxy-instructions)
- [Wireshark with mitmproxy](https://docs.mitmproxy.org/stable/howto-wireshark-tls/)
