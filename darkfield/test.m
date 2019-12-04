%% Lee las imagenes
imgs1=imgLoader(0,'',0,'');
imgs2=imgLoader(0,'',0,'');

%% Revisar el orden en que se importan
ff=imgs1{9,1};%Acá va el Flatfield 5050
ff2=imgs2{9,1};%Acá va el Flatfield 9010

dit_imgs1=imgs1(1:8,:);%Acá los ocho dithering steps 5050
dit_imgs2=imgs2(1:8,:);%Acá los ocho dithering steps 9010

full_image_odd=zeros(256, 256/2*8);%Acá va a guardar la imagen grande odd 5050
full_image_even=zeros(256, 256/2*8);%Acá va a guardar la imagen grande even 5050
full_image_odd2=zeros(256, 256/2*8);%Acá va a guardar la imagen grande odd 9010
full_image_even2=zeros(256, 256/2*8);%Acá va a guardar la imagen grande even 9010

ffeven=zeros(256, 128);%Separa el flatfielf en even 5050
ffodd=zeros(256, 128);%Separa el flatfielf en odd 5050
ffeven2=zeros(256, 128);%Separa el flatfielf en even 9010
ffodd2=zeros(256, 128);%Separa el flatfielf en odd 9010

im_ffodd=ff(:,1:2:256);%Separa el flatfielf en even 5050
im_ffeven=ff(:,2:2:256);%Separa el flatfielf en odd 5050
im_ffodd2=ff(:,1:2:256);%Separa el flatfielf en even 9010
im_ffeven2=ff(:,2:2:256);%Separa el flatfielf en odd 9010
figure;
%sgtitle('Nylon 900um 30kV 180uA');
%Hace el proceso de consturcicón de la imagen grande usando los 8 dithering
%steps
for i=1:8
    im_raw=dit_imgs1{i,1};
    im=imgPepper(FlatField(im_raw,ff,0),0);%Esto hace la corrección de FlatField
    im_odd=im(:,1:2:256);
    subplot(2,4,i);imagesc(im);colormap('gray');%Para que vea cada imagen del dithering step
    im_even=im(:,2:2:256);
    pos=i;
    for col=1:128%Izquierda a derecha
    %for col=128:-1:1%Derecha  a izquierda
        full_image_odd(:,pos)=im_odd(:,col);
        full_image_even(:,pos)=im_even(:,col);
        pos=pos+8;
    end
end

for i=1:8
    im_raw=dit_imgs2{i,1};
    im=imgPepper(FlatField(im_raw,ff2,0),0);%Esto hace la corrección de FlatField
    im_odd2=im(:,1:2:256);
    subplot(2,4,i);imagesc(im);colormap('gray');%Para que vea cada imagen del dithering step
    im_even2=im(:,2:2:256);
    pos=i;
    for col=1:128%Izquierda a derecha
    %for col=128:-1:1%Derecha  a izquierda
        full_image_odd2(:,pos)=im_odd2(:,col);
        full_image_even2(:,pos)=im_even2(:,col);
        pos=pos+8;
    end
end


%% El resto no se qué hace pero no creo que lo necesite
%%

absor=(full_image_odd+full_image_even);%./(im_ffeven+im_ffodd);
phase=(full_image_odd-full_image_even)./(full_image_odd+full_image_even);
absor2=(full_image_odd2+full_image_even2);%./(im_ffeven+im_ffodd);
phase2=(full_image_odd2-full_image_even2)./(full_image_odd2+full_image_even2);
darkfield=(2*(-(55/2*10.^(-6)).^2).*ones(256, 256/2*8)./(-2*log(full_image_odd./full_image_odd2))-(2*log(full_image_even./full_image_odd2)))-(32.65*10^(-6))^2;
%darkfield=-(1/2)*((2*55/2*10.^(-6)).^2)./(log(full_image_odd./full_image_even2)+(log(full_image_even./full_image_even2)))+(32.65*10^(-6))^2;

figure;
%sgtitle('Image of a 600 \mum Nylon - 30kV - 180 \uA');
subplot(1,3,1);
imagesc(absor); colormap('gray');colorbar;title('Absorción');
subplot(1,3,2);
imagesc(phase); colormap('gray');colorbar;title('Fase');
subplot(1,3,3);
imagesc(darkfield); colormap('gray');colorbar;title('Dark field');
%%
figure;
%sgtitle('Image of a 600 \mum Nylon - 30kV - 180 \uA');
subplot(1,3,1);
imagesc(full_image_even); colormap('gray');colorbar;title('Even pixels');
subplot(1,3,2);
imagesc(full_image_odd); colormap('gray');colorbar;title('Odd pixels');
subplot(1,3,3);
imagesc(full_image_odd2); colormap('gray');colorbar;title('Odd pixels 2');
%%
C = imfuse(full_image_even,full_image_odd,'blend','Scaling','joint');
figure;
imagesc(C);title('Nylon 900um 30kV 150uA');colormap('gray');
%%
prof_odd=mean(full_image_odd(106:115,200:800));
prof_even=mean(full_image_even(106:115,200:800));

mean_back_odd=mean(prof_odd(1:200));
mean_back_even=mean(prof_even(1:200));

norm_prof_odd=prof_odd/mean_back_odd;
norm_prof_even=prof_even/mean_back_even;

x=1:1:601;
figure;
subplot(1,2,1);
scatter(x,norm_prof_odd,6,'filled');
hold on;
plot(x, norm_prof_odd);
title('Profile along odd pixels');
subplot(1,2,2);
scatter(x,norm_prof_even, 6, 'filled');
hold on;
plot(x, norm_prof_even);
title('Profile along even pixels');

%%
RAW_abs=imgLoader();
FF_abs=imgLoader(); 
%%
im_abs=RAW_abs{1,1};
ff_abs=FF_abs{1,1};

ffc_abs=imgPepper(FlatField(im_abs,ff_abs),0);
imagesc(ffc_abs);colormap('gray');title('Absorption Image');


