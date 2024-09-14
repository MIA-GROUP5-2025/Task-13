# Task 13.2
# Shape Detection

## Requirements
Detect and classify basic geometric shapes—rectangles, squares, circles, and triangles—and identify their colors. Using classical methods like edge detection, contour analysis, approximation algorithms and geometric properties to identify each shape.

## Our Approach
### Shape Detection

### Color Detection 
We looked up several methods, watched a number of tutorials, and tried to follow them untill we achieved our goal.

## Algorithims and Techniques
### Shape Detection

### Color Detection 
The shapes' colors are determined by RGB value comparison. the function `get_color_name(b, g, r)` takes the pixel's Blue (B), Green (G), and Red (R) values from the image, and then compares them against predefined thresholds to assign a color label. If the red channel is dominant and the green and blue channels are low, it's classified as "Red" and so on. Combinations of high values in several channels are examined for more complicated colors such as Magenta, Yellow, and Cyan. This technique may have trouble with complex or nuanced lighting situations, but it performs well on straightforward images with a small color palette.


## Challenges and Insights
