r = hex(int(input()))
g = hex(int(input()))
b = hex(int(input()))
print('#' +
      r.strip('0x').upper().zfill(2) +
      g.strip('0x').upper().zfill(2) +
      b.strip('0x').upper().zfill(2))
