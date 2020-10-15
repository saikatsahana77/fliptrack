# FlipTrack

> A One-stop Python Package for all info of Flipkart Goods.

---

### Table of Contents

Navigate to your Preferred Section:

- [Description](#description)
- [How To Use](#how-to-use)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This is a package for getting info for Flipakart Products in Python. I have Put  in every information here possible that you need to get of a flipkart with just 1 lines of code. Hope you would enjoy the package.

#### Technologies/Languages Used

- Python

[Back To The Top](#FlipTrack)

---

## How To Use

## Installation

### Windows:

```python3
>>> pip install fliptrack
```

### Mac/Linux:

```python3
>>> sudo pip3 install fliptrack
```

## Usage

```python3
>>> from fliptrack import Fliptrack
```

This will ensure that you have imported the module correctly.

### Now let's explore Different Methods:

1. price

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.price())
   ```

   This takes the link of the product and returns you the price in integer.


2. title

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.title())
   ```

    This takes the link of the product and returns you the title of the product. Return type is str.

3. rating

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.rating())
   ```

   This takes the link of the product and returns you the rating of the product. Return type is float.

4. description

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.description())
   ```

   This takes the link of the product and returns you a short description of the product. Return type is str.

5. mrp

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.mrp())
   ```

   This takes the link of the product and returns you the MRP (Maximum Retail Price) of the product on which the discount is given. Return type is int. If the price and the mrp of the product are same it returns -1.

6. discount

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.discount())
   ```

   This takes the link of the product and returns you the discount percentage if available on the product. Return type is int. If discount id not available it returns -1.


7. seller_name

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.seller_name())
   ```
   This takes the link of the product and returns you the best seller name (recommended by Flipkart) of the product. Return type is str.


8. seller_ratings

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.seller_ratings())
   ```
   This takes the link of the product and returns you the best seller rating (recommended by Flipkart) of the product. Return type is float.

9. highlights

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.highlights())
   ```
   This takes the link of the product and returns you the highlights of the product. Return type is a list of str.

0. ratings_star

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.ratings_star())
   ```
   This takes the link of the product and returns you the number of ratings for each star of the product. Return type is a list of int. Order is from 5 Stars to 1 Star. For getting the value of a particular star however you can pass a optional argument of the star whose value you need to check, if that exists, it will return you the integer value of the number of ratings on that particular star, otherwise it will return the whole list. For example if you want to see how how many people have rated the product 2 star, the code would be as follows:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.ratings_star(2))
   ```

1. ratings_cnt

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.ratings_cnt())
   ```
   This takes the link of the product and returns you the total number of ratings on the product. Return type is int.

2. reviews_cnt

   Usage:

   ```python3
   from fliptrack import Fliptrack
   k = Flipkart(<URL of Product>)
   print(k.reviews_cnt())
   ```
   This takes the link of the product and returns you the total number of reviews on the product. Return type is int.




[Back To The Top](#FlipTrack)

---

## License

MIT License

Copyright (c) [2020] [Saikat Sahana]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#FlipTrack)

---

## Author Info

- Youtube - [Tech Rack](https://www.youtube.com/TechRack)
- Twitter - [@sahana_saikat](https://twitter.com/sahana_saikat)
- Website - [Tech Rack](https://tech-rack.in)
- Facebook - [Saikat Sahana](https://www.facebook.com/saikat.sahana.75)
- Instagram - [saikat2811](https://www.instagram.com/saikat2811/)
- LinkedIn - [Saikat Sahana](https://www.linkedin.com/in/saikat-sahana-454608118)
- Github - [saikatsahana77](https://github.com/saikatsahana77)

[Back To The Top](#FlipTrack)
