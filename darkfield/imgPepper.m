function pxIM = imgPepper( IM,TH )
%function pxIM = imgPepper( IM,TH )
%
%Function that removes dead pixels from an image, and replaces them
%with the average of its 8-neighbours. This removes pepper noise.
%
%pxIM: Corrected image.
%IM: Raw image.
%TH: Cutting threshold to decide the percentage of the max image value that 
%is considered low enough to deem the pixel dead. Values between 0 and 1.


%Author: Gerardo Alfonso Roque Romero
%        High Energy Physics Laboratory
%        Department of Physics, Faculty of Sciences
%        Universidad de los Andes, Bogotá D.C., Colombia.
%        February 1, 2016.


%Variables init
avgIM = 0;
badPx = 0;
pxIM = IM;
imageSize = size( pxIM );
maxIM = max( pxIM(:) );
marker_mask = zeros( imageSize(1) , imageSize(2) );


%Mark the good pixels in the marker_mask, for future usage.
%Get the average value of the image, ignoring bad pixels.
%Bad pixels are those with TH of the value of the maximum
%value present in the image, or less. They are set to 0.
for m = 1:imageSize(1)
    for n = 1:imageSize(2)
        
        if pxIM(m,n) <= (maxIM * TH)
            pxIM(m,n) = 0;
            badPx = badPx + 1;
        else
            marker_mask(m,n) = 1;
            avgIM = avgIM + pxIM(m,n);
        end
        
    end
end

avgIM = avgIM / ( imageSize(1)*imageSize(2) - badPx );


%Replace value of bad pixels with the average
%of its 8-neighbours, dealing with edge pixels.
%When one or more neighbouring pixels are bad,
%ignore them from the neighbour average.
for m = 1:imageSize(1)
    for n = 1:imageSize(2)
	
		%Scan corrected image for bad pixels.
		%If pixel is bad:
		%Extract surrounding pixel 3x3 matrix, excluding
		%bad neighbours and itself. Calculate 3x3 matrix
		%average, ignoring all bad neighbours.
		%If no good pixels exist around current pixel,
		%use the total image average.
        if marker_mask(m,n) == 0
			minicounter = 0;
            minimatrix = zeros(3,3);		

            for i = 1:3
                for j = 1:3

                    %Only address pixels inside image matrix. The rest of positions,
					%replace with 0. Use pixel mask, to ignore bad surrounding pixels.
                    if ( m+2-i ) > 0 && ( m+2-i ) < ( imageSize(1) + 1 ) &&...
                       ( n+2-j ) > 0 && ( n+2-j ) < ( imageSize(2) + 1 )
                   
                        minimatrix(i,j) = pxIM( m+2-i,n+2-j )*...
                                          marker_mask( m+2-i,n+2-j );

                        if minimatrix(i,j) ~= 0
                            minicounter = minicounter + 1;
                        end

                    end

                end
            end
        
			%Get minimatrix average, ignoring ceros.
			%Zeros represent bad pixels, out-of-bounds pixels,
            %and the pixel to be replaced, and must be ignored.
			%If the surrounding 3x3 matrix is filled with 0,
			%use total image average (very unlikely, only on
			%heavily deteriorated or badly uncalibrated sensor).
            if minicounter == 0
                pxIM(m,n) = avgIM;
            else
                pxIM(m,n) = sum( minimatrix(:) ) / minicounter;
            end
            
        end
        
    end
end
