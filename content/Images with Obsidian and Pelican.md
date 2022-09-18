Title: Images with Obsidian and Pelican
Date: 2022-01-05 19:46
Category: Tech	
Tags: Obsidian, Pelican
Summary:A short article on how to work with images so they display correctly in Obsidian and when published with Pelican.

A short article on how to work with images so they display correctly in Obsidian and when published with Pelican.

### Native
This default Obsidian format, with drag and drop into the document, works in Obsidian, but not Pelican.

Obsidian Native: (doesn't work on this site)

`![Obsidian](CleanShot%202022-01-05%20at%2019.30.59@2x.png)`
![Obsidian](CleanShot%202022-01-05%20at%2019.30.59@2x.png)

### Path
Obsidian knows where to find the image, whereas Pelican needs a path added to find the image. In this case `/images/`

Added Path:

`![Added Path](/images/CleanShot%202022-01-05%20at%2019.30.59@2x.png)`
![Added Path](/images/CleanShot%202022-01-05%20at%2019.30.59@2x.png)
 
### Img Tag
But the images are 2x based on the image format and the Retina display it was captured from. It needs to be resized to 50% to display properly. There is not a size option available in Obsidian markdown. You can revert to a standard img html tag to make this work. However, the image will not display in Obsidian.

Use `<img>` tag:

`<img src="/images/CleanShot%202022-01-05%20at%2019.30.59@2x.png" alt="alt text" title="image Title" width="50%"/>`

<img src="/images/CleanShot%202022-01-05%20at%2019.30.59@2x.png" alt="alt text" title="image Title" width="50%"/>

### 1x with Path
The solution is to use images that are 1x sized. Or, set your screen capture tool to 1x, non Retina. This way the images will display correctly in Obsidian and when published with Pelican, with only the path being added manually to the file name.

1x with path added:

`![](/images/CleanShot%202022-01-05%20at%2019.59.47.png)`
![](/images/CleanShot%202022-01-05%20at%2019.59.47.png)

### Automation

What automation tools are available in Pelican to automatically reformat and resize the images?

To be continued....