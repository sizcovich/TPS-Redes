echo %date% ; %time% ; Atlantis-2 ; ping >> ping_Atlantis.txt
ping 94.142.121.249 -n 12 >> ping_Atlantis.txt
ping 94.142.126.214 -n 12 >> ping_Atlantis.txt

echo %date% ; %time% ; Atlantis-2 ; trace >> trace_Atlantis.txt
tracert 62.28.158.193 >> trace_Atlantis.txt
tracert 62.28.158.203 >> trace_Atlantis.txt

echo %date% ; %time% ; Tata ; ping >> ping_Tata.txt
ping 66.198.70.1 -n 12 >> ping_Tata.txt
ping 80.231.130.33 -n 12 >> ping_Tata.txt

echo %date% ; %time% ; Tata ; trace >> trace_Tata.txt
tracert 212.30.252.35 >> trace_Tata.txt
tracert 212.30.252.32 >> trace_Tata.txt
tracert 212.30.252.27 >> trace_Tata.txt

echo %date% ; %time% ; Southern Cross Cable Network ; ping >> ping_Southern_Cross.txt
ping 67.17.192.6 -n 12 >> ping_Southern_Cross.txt
ping 203.208.192.82 -n 12 >> ping_Southern_Cross.txt

echo %date% ; %time% ; Southern Cross Cable Network ; trace >> trace_Southern_Cross.txt
tracert 202.62.118.46 >> trace_Southern_Cross.txt
tracert 202.62.118.47 >> trace_Southern_Cross.txt
tracert 202.62.118.48 >> trace_Southern_Cross.txt

