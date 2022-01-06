Title: Use Prism for Syntax Highlighting in Ghost
Date: 2020-10-05 03:00
Author: D
Category: Tech
Tags: Ghost, Tech
Slug: use-prism-for-syntax-highlighting-in-ghost

Configure Ghost and Prism to provide code syntax highlighting for all popular formats including javascript, php, html, css, markdown and more.

Ghost is a great CMS and it's easy to add a code syntax highlighter such as [Prism](https://prismjs.com/).

## Versions

Ghost version 3.3  
Prism version 1.21

## Prism

There are two ways to use Prism: 1) download and serve from your website or 2) serve from a [Content Delivery network (CDN)](https://en.wikipedia.org/wiki/Content_delivery_network). The CDN option is actually easier and better for your viewers. There is a chance that many sites use Prism and once your browser has it in its local cache it won't need to download it again, which makes it faster and uses less bandwidth. So, that's what you will learn about today.

**Step 1** - Go to the [Prism](https://prismjs.com/) website and learn a little about it. Look at the Theme bubbles down the right-side of the page. Find a theme that you like and want to use on your Ghost powered blog. I use the "Okaidia" theme on this website. Also, notice that there are many, many language features supported. If you will always just use a few languages then you can hard code them into your setting and only use them. However, if like me there is no telling which language you will post about next then you should use the autoloader feature.

Take note of the latest Prism version. As of this writting I'm using version 1.21.0. You will want to use the most current version.

## CDN

**Step 2** - Find a CDN that hosts Prism. I chose [cdnjs.com](https://cdnjs.com/) to serve the Prism files. It's free, easy to use and fast. I recommend you go to [cdnjs.com](https://cdnjs.com/) and search for Prism. You will see that there are a lot of options. You don't need all of those, just the ones you are interested in.

**Step 3** - There are 3 main parts of Prism you need to make this work. The first part is the CSS. To load this from cdnjs.com looks like this.

Part 1: Choose your theme:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.21.0/themes/prism-okaidia.min.css">
```

Link to Prism okaidia theme

Notice this version contains the word `okaidia` which means it has the color scheme for the Theme I like. You should search for the Theme that you chose in step 1.

Part 2: Find the core js file:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.21.0/components/prism-core.min.js"></script>
```

Link to Prism core library

It contains the `core` of the Prism library.

Part 3: Find the language modules you want to use, or find the [`autoloader`](https://prismjs.com/plugins/autoloader/) version.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.21.0/plugins/autoloader/prism-autoloader.min.js"></script>
```

Link to Prism autoloader

These are the 3 minimum components needed to use Prism with Ghost.

Now that you have identified the 3 main components and their links to the CDN, it's time to put them into your Ghost blog.

## Code Injection

Ghost makes this very easy to do with the `Code injection` feature on their admin page.

**Step 4** - Go to your ghost admin page, it is defaulted to site.tld/ghost, and login with your admin account.

Click on the `Code injection` menu option on the left. You should see two main sections "Site Header" and "Site Footer".

Part 1 - Place the CSS link in the `Site Header` section. It should look something like this:

![](https://ghost.64zbit.com/content/images/2020/10/image.png)

Site Header portion of Code injection

That's all there is, just copy and paste the above CSS link into the `Site Header` section.

Part 2 - The `Site Footer` works the same, just copy and paste the `core` link and the `autoloader` link. If you decided to go with language specific options this is where you would load them instead of the autoloader link.

Remember these links are loaded on every page of your blog even if you don't use them on that page, so keep it simple, small and fast.

![](https://ghost.64zbit.com/content/images/2020/10/image-1.png)

Site Footer portion of Code injection

## Configuration Complete

That's all there is to configuring Ghost to use Prism. The next portion will show you how to use them on your blog.

**Step 1** - Create a new post in Ghost and press the + icon to add a new section to your page, and then immediately type ``` <enter> that's 3 back-tick special characters under the ~ symbol on the top left of your keyboard. They are not single quotes ' or double quotes ".

This puts Ghost into the code entry mode. You can copy and paste your code in here.

**Step 2 -** Notice on the right hand side of the code entry box there is a place for language. This is where you type in the language for this code snippet. Ghost has done some of the work for you. You don't have to prepend the language type with `language-` or `lang-` as talked about in the Prism documentation, just put in what you are working with. Such as: js, javascript, html, php, json, css, etc..

![](https://ghost.64zbit.com/content/images/2020/10/image-2.png)

Sample html script with language type shown in top-right corner

That's it! You code snippets will now be syntax highlighted with Prism.

## Further Reading

For more examples and tips on how to add line numbers and a copy-to-clipboard button check out this [Ghost tutorial](https://ghost.org/tutorials/code-syntax-highlighting/).

## Examples

Here are a few examples to look at.

```js
function createBoard(team) {

    let out = "";
    out += "<div class='text-center'>";
    for (col = 1; col <= 10; col++) {
        for (row = 1; row <= 10; row++) {
            let calcId = team + "-" + zeroPad(row, 2) + zeroPad(col, 2);
            let link = ` '${team}', ${row}, ${col}, '${calcId}'`;
            out += `  <a class='m-0 p-1 btn btn-dark' href="javascript:fire(${link});" role='button'>`
            out += "   <span class='title'>";
            out += "    <span id='" + calcId + "' class='badge badge-dark oi' data-glyph='target'>" + " " + "</span>";
            out += "   </span>";
            out += "  </a>";
        }
        out += " <br> ";
    }
    out += "</div>";

    $('#board-' + team).html(out);

}
```

Sample Javascript code

```css
@import "ios.css";
/* @import "darkMode.css"; */
@import "toggleSwitch.css";

@font-face {
    font-family: Revamped;
    src: url("../font/Revamped.ttf") format('truetype');
}

/* get screen width based on device */
:root {
    /* desktop vars */
    --screen-w1: 500px;
    --screen-w2: 495px;
}

@media screen and (max-width: 500px) {
    :root {
        /* mobile vars */
        --screen-w1: 97vw;
        --screen-w2: 94vw;
    }
}
```

Sample CSS code

```php
public function getGame($userName, $roomName, $gameToken)
    {

        //load game
        $this->game = $this->loadGame($gameToken);

        return $this->game;
    }
```

Sample PHP code

```html
<!-- Main Nav Bar -->
        <div class="w3-top hide main">
            <div class="w3-bar w3-round-large z-nav-background z-width" xstyle="max-width:500px">
                <span class="">
                    <a onclick="showPanel('lobby')" class="w3-bar-item w3-round-large z-nav-text">Lobby</a>
                </span>

                <button onclick="showPanel('E-Space')" class="w3-button z-nav-text w3-border w3-border-blue w3-hover-black w3-small">E-Space</button>
                <button onclick="showPanel('F-Space')" class="w3-button z-nav-text w3-border w3-border-blue w3-hover-black w3-small">F-Space</button>

            </div>
        </div>
```

Sample HTML code

```sql
ALTER TABLE `activeUserTable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `time_index` (`time`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activeUserTable`
--
ALTER TABLE `activeUserTable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;
```

Sample SQL code