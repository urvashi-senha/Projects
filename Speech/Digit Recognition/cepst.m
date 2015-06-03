function c=cepst(s,fs,N,M,L)
% convert speech waveform to sets of L cepstral coefficients using
% frames of length N samples, with frame shifts of M samples

    NFFT=1024;
    es=length(s);
    ss=1;
    c=[];
    while ss+N-1 <= es
        sf=ss+N-1;
        frame=s(ss:sf)'.*hamming(sf-ss+1)';
        frame=[frame zeros(1,NFFT-N)];
        sp=log(abs(fft(frame,NFFT)+0.00000001));
        cep=real(ifft(sp,NFFT));
        if (sum(cep(2:L+1).^2) >0)
            c=[c; cep(2:L+1)];
        end
        ss=ss+M;
    end