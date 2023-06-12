## Blog site using GitHub Pages and Jekyll
> This site is intended for Teachers.   This is to build lessons and distribute across different sections.
- This support 3 computer science sections that are in a pathway (JavaScript, Python/Flask, Java/Spring)
- JavaScript documents are new material for entry class into the pathway, they are prerequisites for the Python and Java classes.
- All course material works off of Notebooks using Python kernel, except Java which requires it own kernel.

## Preview Site 
> GitHub Pages development is optimized by testing and developing on your local machine.  This is called previewing you work, prior to commit and push.

- Install for Ubuntu using apt
```bash
# ruby
sudo apt install ruby-full build-essential zlib1g-dev
# avoid root user, set up a gem installation directory for your user account
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
# install jekyll and bundler
gem install jekyll bundler
```
- Install for MacOS using brew
```bash
# ruby
brew install chruby ruby-install xz
ruby-install ruby 3.1.3
# configure ruby into shell .zshrc or change to .bash_profile
echo "source $(brew --prefix)/opt/chruby/share/chruby/chruby.sh" >> ~/.zshrc
echo "source $(brew --prefix)/opt/chruby/share/chruby/auto.sh" >> ~/.zshrc
echo "chruby ruby-3.1.3" >> ~/.zshrc # run 'chruby' to see actual version
#
# quit and relaunch terminal
#
# install jekyll
gem install jekyll
```




```bash
bundle install
```
- Now the project is ready for preview.  To simplify typing and sharing logging the details for running have be place in a ```Makefile```
    - run preview server
    ```bash
    make
    ```
    - stop preview server
    ```bash
    make stop
    ```
    - test notebook conversions
    ```bash
    make convert
    ```
    - clean constructed files
    ```bash
    make clean
    ```
