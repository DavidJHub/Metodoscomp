function imageStack = imgLoader( prefixFlag , prefixString , interFlag , autoPath )
%imageStack = imgLoader( prefixFlag , prefixString , interFlag , autoPath )
%
%Loads all .txt files in the directory selected by the user, and stores 
%them in a cell array. Depending on the prefixFlag, the function loads
%files that begin the filename with the specified prefix stored on
%prefixString.
%
%Depending on interFlag, the routine will call the UI for the user to
%choose the load path. Otherwise, it will take the path from the input
%autoPath.
%
%It expects matrices with ASCII, non-negative
%numbers. Returns the cell array with all the images, loaded in 
%alphabetical order, with names.
%
%
%INPUTS:
% prefixFlag: To decide whether to load selectively. 1: Load files with
% prefix defined in prefixString. Other value: load everything in the
% path.
%
% prefixString: String where the prefix is defined.
%
% interFlag: To decide whether to make the user choose the load path, or
% take it from the input variable autoPath. 1: autoload. Other: ask for
% path using UI.
%
% autoPath: String with the load path, in case the user chooses to use this
% function unattended.
%
%
%OUTPUTS:
% imageStack{k,1}: image matrix, in grayscale.
% imageStack{k,2}: image filename, in string, without file extension.


%Author: Gerardo Alfonso Roque Romero
%        High Energy Physics Laboratory
%        Department of Physics, Faculty of Sciences
%        Universidad de los Andes, Bogotá D.C., Colombia.

%%Log Change.
% V1.0. June 1, 2016.
% Initial revision.
%
% V1.1. November 29, 2017.
% Added uigetdir, so the user can select a directory with the GUI and
% mouse, instead of inputing a path in a string manually.
%
% V2.0. August 13, 2018.
% Added prefix finder, to load only files that have a defined prefix.
% Added option for autoloading, or make the user choose the load path.



%Ask the user to select the folder where the files to be loaded reside.
%Depending on the interFlag.
if interFlag
    imPath = autoPath;
else
    imPath = uigetdir( '/home/q507/Documents/Usuarios', ...
             'Select the source directory');
end

%File list of .txt images will be loaded onto "fileNames".
%Works on the current working directory.


%If the prefixFlag is on, load only the files beginning with the prefix
%set on prefixString, from the imPath.
%If the prefixFlag is off, load everything on the imPath.
if prefixFlag == 1
    %Construct the filenames to search.
    %Search and load only the filenames containing the prefix.
    %filenameString = strcat( prefixString , '*.tif' );
    filenameString = strcat( '*', prefixString , '.txt' );
else
    filenameString = '*.txt';
    %filenameString = '*.tif';
end

%Define the files to load.
fileNames = dir( fullfile( imPath, filenameString ) );
fileNames = {fileNames.name};

%Sort the File Names in Natural order: 1,2,3...,9,10, instead of
%1,10,11,12,... etc. It uses a third-party sorting function, natsortfiles.
fileNames = natsortfiles( fileNames );

%Load.
imageStack = cell( numel( fileNames ),2 );
for i = 1 : numel( fileNames )

    %imageStack{i,1} = imread( strcat( imPath,'/',fileNames{i} ) , 'tif' );
    imageStack{i,1} = dlmread( strcat( imPath,'/',fileNames{i} ) , ' ' );
    [~,imageStack{i,2},~] = fileparts( fileNames{i} );
    imageStack{i,1} = imageStack{i,1}';

end