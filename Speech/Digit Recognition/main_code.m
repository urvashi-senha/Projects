function main_code(tdigit)
    fsout=8000;
    Lm=40; % frame size
    L=320;
    Rm=10; % frame shift
    R=80;
    Lcep=12; % cepstral co-ef
    ibest=-1; % answer
    i2best=-1; % answer
    dbest=-1; % answer distance score
    d2best=-2; % answer2 distance score
    
   
%     tdigit=4 ;% test digit
    tindex = 2;
    
    filetest=['test/',num2str(tdigit),num2str(tindex),'.wav'];
    % sampling test file -  stest
    
    [stest,fs]=audioread(filetest);
   sound(stest,fs);
    %co -eff
    ctest=cepst(stest,fs,L,R,Lcep);
    ntest=length(ctest);
  % best distances and digits
    dbest=1.e5; d2best=1.e5; ibest=0; i2best=0;
        
    for idigit=1:9
        fileref=['train/',num2str(idigit),num2str(tindex),'.wav'];
  
% sampling training file - sref
    
    	[sref,fs]=audioread(fileref);
    	%co-eff
    	cref=cepst(sref,fs,L,R,Lcep);
    	nref=length(cref);
    

    
% compare test and reference patterns using simple dtw
    %[distance,paths,distances]=dtw_backtrack_dist(cref,nref,ctest,ntest,Lcep);
   % distances=distances/ntest;
    
	distance = dtw_new(cref,ctest);
	

% keep track of best and second best distances and digits
    if (distance < dbest)
        d2best=dbest;
        i2best=ibest;
        dbest=distance;
        ibest=idigit;
    elseif (distance > dbest & distance < d2best)
        d2best=distance;
        i2best=idigit;
    end
    

    end
   display('test digit');
   disp(tdigit);
    
    display('Output digit');
    disp(ibest);
    
    display('Output digit distance');
    disp(dbest);
    display('2nd best Output digit');
    disp(i2best);
    
    
    switch ibest
        case 1
            display('One - January')
    case 2
            display('Two - February')
        case 3
            display('Three - March')
        case 4
             display('Four - April')
        case 5
            display('Five- May')
        case 6
            display('Six - June')
        case 7
            display('Seven - July')
        case 8
            display('Eight - August')
        case 9
            display('Nine - September')
 end
