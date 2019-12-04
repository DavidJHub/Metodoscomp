function flatIM = FlatField(IM,FF,logSW)
%flatIM = FlatField(IM,FF,sw)
%
%Flat Field Correction of an image, using the formula:
%
%  C = ln( F/I )
%
%where:
%C: Corrected Image.
%I: Raw Image.
%F: Flat Field Image.
%
%flatIM: Corrected image, ASCII matrix.
%IM: Unprocessed image.
%FF: Flat-Field correction mask.
%logSW: 1: Apply Log to the flat field. Other: Don't apply Log.


%Author: Gerardo Alfonso Roque Romero
%        High Energy Physics Laboratory
%        Department of Physics, Faculty of Sciences
%        Universidad de los Andes, Bogotá D.C., Colombia.
%        February 1, 2016.
%
%ChangeLog:
%V1.1: May 15, 2019.
%Added a switch to allow user to select if the final LOG is applied to the
%corrected data, or not.

%Variables init
imageSize = [ size(IM,1) , size(IM,2) ];

%Correct input image with Flat-Field image.

%Form #1:
%avgFF =  sum( FF(:) ) / ( imageSize(1)*imageSize(2) );
%flatIM = log( IM ./ ( FF/avgFF ) );

%Form #2:
%FF_norm = FF./( max( max( FF ) ) );
%flatIM = log( IM ./ FF_norm );

%Form #3:
if logSW == 1
    flatIM = -log( IM ./ FF );
else
    flatIM = ( IM ./ FF );
end


%Corrections for ill-calculated corrected values. This eliminates all Inf
%(good pixels, with 0 value in the image), -Infs (bad pixels with 0 value
%in the FF mask, with positive values in the image), and NaNs (bad pixels
%with 0 value in the FF mask and image).
%
%This will replace:
%   Infs with the max value of the image.
%   -Infs and NaNs with 0 (nonsense data coming from dead pixels).

%Step #1:
%Find the maximum valid value of the image. This means, a value that is
%not Inf. Replace NaNs and -Infs with 0.
%Find values that are less than 0, but not -Inf. These values are those
%that appear less bright in the FF image, than in the RAW (theoretically
%makes no sense, but statistical fluctuations can make this happen
%slightly, and make the imgPepper algorithm fail on these pixels). These
%values are ase having the same absorption as open beam, thus put them the
%smallest possible value that is not 0.
maxIM = 0;
for i = 1:imageSize(1)
for j = 1:imageSize(2)
    
    if flatIM(i,j) > maxIM && ~isinf( flatIM(i,j) )
        maxIM = flatIM(i,j);
    end
    if isnan( flatIM(i,j) ) || isinf( -flatIM(i,j) )
        flatIM(i,j) = 0;
    end
    if flatIM(i,j) < 0 && ~isinf( -flatIM(i,j) )
        flatIM(i,j) = eps;
    end
end
end

%Step #2:
%Replace Infs with Max value. As, presumably, nothing can be more absorbing
%than the most absorbing part of the image, it doesn't make sense to have a
%value above the maximum value. All pixels corrected to values beyond this
%maximum will be clamped to said value. This could be refined to include
%weighting by the FF mask: the maximum value is taken from some pixel, with
%a corresponding FF value, that could be renormalized using the FF value
%for the pixel to correct, in order to have a more accurate extrapolated
%correction. It still does not make too much sense all the effort, since
%we are trying to correct for a total lack of data in this case.
for i = 1:imageSize(1)
for j = 1:imageSize(2)

    if isinf( flatIM(i,j) )
        flatIM(i,j) = maxIM;
    end
    
end
end


end