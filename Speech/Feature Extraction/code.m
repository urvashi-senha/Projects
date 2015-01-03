%% Reading wave file

[sample,fs] = audioread('sample.wav');

binary_array =  dec2bin(typecast(sample(:,1),'uint8'),8);

%% Plotting wave file
% left=sample(:,1);
% time = (1/fs)*length(left);
% t = linspace(0,time,length(left));
% plot(t,left);

%% Diving into frames

frame_time = 0.02;
N = length(sample);
frame_len = fs*frame_time;
frame_no = floor(N/frame_len);

a = dsp.ZeroCrossingDetector;
array = [];
array_1 = [];
array_2 = [];
array_3 = [];

en= [];


Voiced_Frames = [];
Unvoiced_Frames = [];
Voiced_Zero_Crossings = [];
Unvoiced_Zero_Crossings = [];
Voiced_LPC = [];
Unvoiced_LPC = [];

%% Analysis


for k=1 : frame_no
    
    frame0 = sample( (k-1)*frame_len +1 : k*frame_len );
    nfft = 2^nextpow2(frame_len);
    frame1 = filter([1, -0.97], [1], frame0);
    ham_frame = frame1' .* hamming(frame_len);
    frame1= frame1 .* hamming(frame_len)';
    
    
    %%    Time Domain Feature Analysis
    
    energy = frame0.^2;
    zc = step(a,ham_frame);
    en = [ en ; max(energy) ];
    
    %%     LPC analysis
    
    
    [c,e] = lpc(frame1,12);
    
    %% Energy
    
    if max(energy) > 0.005
        Voiced_Frames = [Voiced_Frames k];
        Voiced_Zero_Crossings = [ Voiced_Zero_Crossings zc ];
        Voiced_LPC = [Voiced_LPC c(1,2)];
        
    else
        
        Unvoiced_Frames = [Unvoiced_Frames k];
        Unvoiced_Zero_Crossings = [ Unvoiced_Zero_Crossings zc ];
        Unvoiced_LPC = [ Unvoiced_LPC c(1,2) ];
        
    end
    
    
    
    
    
    %%    Spectral Analysis
    spectrum = fft(frame1,nfft);
    logmagspec = log(abs(spectrum)+eps);
    cepstrum = ifft(logmagspec,nfft);
    
    cepstrum_low =[cepstrum(2:30) zeros(1,227)];
    cepstrum_high =[zeros(1,30) cepstrum(31:257)];
    
    log_low = fft(cepstrum_low,nfft);
    log_high = fft(cepstrum_high,nfft);
    
    % Graphs
    
    %      figure();
    %       subplot(2,2,1);
    %       title('log magnitude spectrum');
    %       plot(logmagspec);
    %       subplot(2,2,3);
    %       title('Spectral Envelope');
    %       plot(abs(log_low));
    %       subplot(2,2,4);
    %       title('Spectral details');
    %       plot(abs(log_high));
    
    
    %%    Resynthesize signal
    array_1 = [ array_1  (ifft(spectrum))];
    array_2 = [array_2 (ifft(angle(spectrum)))];
    array_3 = [array_3 (ifft(abs(spectrum)))];
    
    r1 = filter(c,1,frame1);
    r2 = filter(1,c,r1);
    array = [ array r2 ];
    %
    
end


%% Mel-Cepstrum Coefficients

MFCC = mfcc(sample,fs,25,10,0.97,[300 3700],20,20,22);

%plot(MFCC);

%% Resynthesis Plot
% Resynthesize signal using IFFT(same magnitude and same phase)
% figure();
% plot((array_1));
% Resynthesize signal using IFFT(same magnitude and unit phase)
% figure();
% plot(abs(array_2));
% Resynthesize signal using IFFT(same magnitude and unit phase)
% figure();
% plot((array_3));





%%               OBSERVATIONS:

% ZC: 190 and above indicate UNVOICED regions.
%
% LPC: -3.2741 to -0.4602 indicate VOICED regions
%      0.1449 to  -2.8705 indicate UNVOICED regions
%
% ENERGY: 0.005 and above indicate VOICED regions
%
% If the energy level and zero-crossing rate of 3 successive frames is high it is a starting point.
% After the starting point if the energy and zero-crossing rate for 5 successive frames are low it is the end point.
% 

