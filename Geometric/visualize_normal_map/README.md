# visualize_normal_map

 <table align="center">
  <tr>
    <td><img src="./images/scan2_vid2.png" width="400" height="300"></td>
    <td><img src="./images/scan2_vid2_depth.jpg" width="400" height="300"></td>
  </tr>
  <tr>
    <td>scan2 vid2</td>
    <td>depth map</td>
  </tr>
   <tr>
    <td><img src="./images/scan2_vid2_normal.jpg" width="400" height="300"></td>
    <td><img src="./images/depth2normal_masked.jpg" width="400" height="300"></td>
  </tr>
  <tr>
    <td>normal map</td>
    <td>depth-to-normal (masked)</td>
  </tr>
</table>

### Usage:
`python gray2color_normal.py ./colmap_data/scan2_vid2_normal.bin`


### Note:
+ normal map Visualization: reverse and l2-normalized
+ depth-to-normal using [method](https://github.com/XiWJ/tricks/tree/master/ComputeNormal) with K_size=5
