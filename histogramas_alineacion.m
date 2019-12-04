ruta1='E:\Documentos\Usuarios\2019-20\David Jurado (Intermedio)\Alineacion 2\H2';
%ruta2='E:\Documentos\Usuarios\2019-10\Carlos Navarrete (Fisica)\2019-07-16 Nylon 900um 180cm Si\SMEI_same_statistics\Mask alignment 2';
imgs=imgLoader(0,'',1,ruta1);
%imgs=imgLoader(0,'',0,'');
%%
figure;
step=338;   
for i=1:12
    imagen=imgs{i,1};
    even=imagen(:,2:2:end);
    odd=imagen(:,1:2:end);
    subplot(6,2,i);
    histogram(even,60);
    hold on;
    h=histogram(odd,60);
    h.FaceAlpha=0.5;
    title(num2str(i));
    step=338+(i*2);
end

%%
imgs2=imgLoader(1,'txt_Event',0,'');
%%
figure;
step=380;
for i=1:11
    imagen=imgs2{i,1};
    even=imagen(:,2:2:end);
    odd=imagen(:,1:2:end);
    subplot(6,2,i);
    histogram(even,60);
    hold on;
    h=histogram(odd,60);
    h.FaceAlpha=0.5;    
    title(num2str(step));
    step=380+(i*5);
end