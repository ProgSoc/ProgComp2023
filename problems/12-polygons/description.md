# Polygon Union

You are working on a custom slicer for a 3D printer. However, you've noticed an edge case where some STL files contain overlapping shapes, which causes weird bugs in your code.

So the solution you've come up with, is for each slice, to find the union of all the polygons in the slice. This way, you can be sure that the polygons are non-overlapping. Couldn't be that hard, right?

## Some context

I'm sure everyone knows what a 3D printer is. However, a "slicer" is the software that takes a 3D model, and converts it into a set of instructions for the printer to follow. The printer then follows these instructions, and prints the model. This process generally involves "slicing" the 3D model into layers first, hence the name.

![Slicer visualization](_images/slicer.png)

Each layer of the sliced model gets converted into a path that the printer can follow (a series of lines and curves).

<img src="_images/print.png" height="300px">

However, to have an effective way to convert the slice into a path, you need to make sure that you don't have any overlapping geometry or other weird artifacts. The overlapping geometry part is what you're trying to solve here.

## The problem

You have 2 polygons A and B, which are both simple polygons. For now, you assume that the polygons are:

- Convex
- All points are oriented clockwise (each point is in a clockwise direction from the previous point)
- Definitely overlapping
- There is only 2 line intersections in each test case, to make this easier. A polygon's line goes into the other one and then exits.

**We are going to ignore edge cases, such as:**

- The polygons are the same
- The polygons are disjoint
- 2 points of the the polygons are in the same coordinate
- 2 lines are colinear

All of these edge cases can be considered in the future (after the competition :) ), but for now you want to just have a proof of concept algorithm.

Your task is to find the union of these 2 polygons. For the tests, you should just output the area of the union, using the "polygon area" function that's provided in the scaffolds.

<details>
<summary>What's a "convex polygon"?</summary>

A convex polygon is a polygon that has no concave angles. In other words, if you take any 2 points on the polygon, the line segment between them will be contained within the polygon.

As you can see in the below image, if we draw a line between the 2 bottom points of the concave polygon, the line segment will be outside of the polygon.

![Convex polygon](_images/convex.png)

</details>

For example, here are 2 polygons (from the sample test cases):

![Example polygons](_images/polygons1.png)

Their union will look like the following:

![Example polygons](_images/polygons3.png)

The total area of the union is `105`, because the square is `100` and the appended triangle is `5`.

<details>
<summary>Another example</summary>

Here is another example:

![Example polygons](_images/polygons4.png)

Their union will look like the following:

![Example polygons](_images/polygons5.png)

With the total area being `175`, as the two squares are `100` each, with their overlap being `25`.

</details>

## Input

The input will be 2 polygons, each represented as a list of points. Each point will be represented as a tuple of 2 integers, representing the x and y coordinates of the point.

The points will be given in clockwise order. All of the points will be integers.

## Output

The output should be a single decimal, representing the area of the union of the 2 polygons.
