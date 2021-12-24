# visualize_normal_map

 <table align="center">
  <tr>
    <td><img src="https://github.com/XYZ-qiyh/Visualization-in-python-Vip/blob/master/visualize_normal_map/images/scan2_vid2.png" width="400" height="300"></td>
    <td><img src="https://github.com/XYZ-qiyh/Visualization-in-python-Vip/blob/master/visualize_normal_map/images/scan2_vid2_depth.jpg" width="400" height="300"></td>
  </tr>
  <tr>
    <td>scan2 vid2</td>
    <td>depth map</td>
  </tr>
   <tr>
    <td><img src="https://github.com/XYZ-qiyh/Visualization-in-python-Vip/blob/master/visualize_normal_map/images/scan2_vid2_normal.jpg" width="400" height="300"></td>
    <td><img src="https://github.com/XYZ-qiyh/Visualization-in-python-Vip/blob/master/visualize_normal_map/images/depth2normal.jpg" width="400" height="300"></td>
  </tr>
  <tr>
    <td>normal map</td>
    <td>depth-to-normal</td>
  </tr>
</table>

### Usage:
`python gray2color_normal.py ./colmap_data/scan2_vid2_normal.bin`


### Note:
+ normal map Visualization: reverse and l2-normalized
+ depth-to-normal using [method](https://github.com/XiWJ/tricks/tree/master/ComputeNormal) with K_size=5
