# ❤ Contributing

Found a bug? Have a good idea for improving Theia? Head over to Theia's 
Github page and create and submit a new issues/feature request. Want 
to contribute your code? Go to the [contributing code]() section and
submit a pull-request.

## Feature request or bug report

Found a bug or have a feature request go to our 
[issue-tracker](https://github.com/mikevansighem/theia/issues) and report
it using the appropriate template.

## Writing documentation

Want to contribute to our documentation? Your a real hero! 🎉
Our documentation is all written in Markdown and build by 
[MkDocs](https://www.mkdocs.org/) To add pages to our documentation place 
your new markdown file in `\docs` and add the page in the `nav` section 
of `.mkdocs.yml`. Have you added any images, place these in `\docs\images`.
To preview the changes navigate to the root of the repository and run:

```bash
mkdocs serve
```

!!! warning
    If the website does not load immediately you should refresh the webpage
    once the the site has been build end the local server is running.

## Contributing code

Want to contribute your coding skills? Head over tot our 
[issue-tracker](https://github.com/mikevansighem/theia/issues) and
look for an issue/feature you like to work on. All-ready have your code written?
No need to file an issue first immediately create an pull-request.

### Pull-request process

Once you create a pull-request your code code will be checked by our 
CI system. To find out which checks are being run head over to the 
[testing]() page. 
If all the checks pass one of the core-contributers will accept you 
pull-request and merge it with the master branch to be deployed.

### Code style

The code style we use is ["Black"](https://github.com/ambv/black), but 
don't worry about that to much as long as you have the provided 
[pre-commit hooks]() installed there is nothing for you to do. Black 
takes over the minutiae of hand-formatting. One thing Black cannot solve
is your variable naming. Please keep these according to 
[PEP-8](https://www.python.org/dev/peps/pep-0008/). 

### Commit messages

Inspired by [Gitmoji](https://gitmoji.carloscuesta.me/) we like all our 
commit messages to be preceded by an emoji. Using emoji on commit 
messages provides an easy way of identifying the purpose or intention 
of a commit with only looking at the emoji used. Refer to the table 
underneath to see which emoji is appropriate for your commit.

| Emoji               		| Commit type                   | Code               	    |
|:-------------------------:|:------------------------------|:--------------------------|
| :tada:					| Initial commit             	| `:tada:`              	|
| :sparkles:				| New feature                	| `:sparkles:`          	|
| :white_check_mark:		| Adding a test              	| `:white_check_mark:`  	|
| :memo:					| Writing documentation      	| `:memo:`              	|
| :bulb:					| Documenting source code    	| `:bulb:`              	|
| :hankey:					| Bad code                   	| `:hankey:`            	|
| :alembic:					| Experimental stuff         	| `:alembic:`           	|
| :construction:			| Work in progress           	| `:construction:`      	|
| :lipstick:				| Updating UI or style files 	| `:lipstick:`          	|
| :recycle:					| Refactoring code           	| `:recycle:`           	|
| :art:						| Improve format/structure   	| `:art:`               	|
| :zap:						| Performance improvement    	| `:zap:`               	|
| :rotating_light:			| Removing linter warnings   	| `:rotating_light:`    	|
| :beetle:					| Bugfix                     	| `:beetle:`            	|
| :lock:					| Fixed security issue       	| `:lock:`              	|
| :penguin:					| Fixing on Linux            	| `:penguin:`           	|
| :apple:					| Fixing on MacOS            	| `:apple:`             	|
| :checkered_flag:			| Fixing on Windows          	| `:checkered_flag:`    	|
| :truck:					| Moving files/code          	| `:truck:`             	|
| :wastebasket:				| Removing code/files        	| `:wastebasket:`		    |
| :heavy_plus_sign:		 	| Adding a dependency        	| `:heavy_plus_sign:`	    |
| :heavy_minus_sign:		| Removing a dependency      	| `:heavy_minus_sign:`	    |
| :arrow_up:				| Upgrading dependencies     	| `:arrow_up:` 			    |
| :arrow_down: 				| Downgrading dependencies   	| `:arrow_down:`		    |
| :wrench:					| Configuration files        	| `:wrench:`				|
| :card_index: 				| Metadata                   	| `:card_index:`		    |
| :bookmark:				| Releasing or version tags  	| `:bookmark:`			    |
| :rocket:					| Deploying stuff            	| `:rocket:`				|
| :twisted_rightwards_arrows:| Merging branches         | `:twisted_rightwards_arrows:` |
| :rewind:					| Reverting changes          	| `:rewind:`			    |
