%% Lee las imagenes
imgs=imgLoader(0,'',0,'');
%% Revisar el orden en que se importan
ff=imgs{9,1};%Acá va el Flatfield
dit_imgs=imgs(1:8,:);%Acá los ocho dithering steps
full_image_odd=zeros(256, 256/2*8);%Acá va a guardar la imagen grande odd
full_image_even=zeros(256, 256/2*8);%Acá va a guardar la imagen grande odd
ffeven=zeros(256, 128);%Separa el flatfielf en even
ffodd=zeros(256, 128);%Separa el flatfielf en even
im_ffodd=ff(:,1:2:256);%Separa el flatfielf en even
im_ffeven=ff(:,2:2:256);%Separa el flatfielf en even
figure;
%sgtitle('Nylon 900um 30kV 180uA');
%Hace el proceso de consturcicón de la imagen grande usando los 8 dithering
%steps
for i=1:8
    im_raw=dit_imgs{i,1};
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

%% El resto no se qué hace pero no creo que lo necesite
%%

absor=(full_image_odd+full_image_even)%./(im_ffeven+im_ffodd);
phase=(full_image_odd-full_image_even)./(full_image_odd+full_image_even);
figure;
%sgtitle('Image of a 600 \mum Nylon - 30kV - 180 \uA');
subplot(1,2,1);
imagesc(absor); colormap('gray');colorbar;title('Absorción');
subplot(1,2,2);
imagesc(phase); colormap('gray');colorbar;title('Fase');
%%
figure;
%sgtitle('Image of a 600 \mum Nylon - 30kV - 180 \uA');
subplot(1,2,1);
imagesc(full_image_even); colormap('gray');colorbar;title('Even pixels');
subplot(1,2,2);
imagesc(full_image_odd); colormap('gray');colorbar;title('Odd pixels');
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


