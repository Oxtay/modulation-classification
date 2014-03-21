def modulator():
    K = 2^constel
    x = randintvec(n,K)        # Create a signal source for PSK.
    h = modem.qammod('M',K,'PhaseOffset',0,'SymbolOrder','binary')
    y = modulate(h,x)          # Modulate the signal x.