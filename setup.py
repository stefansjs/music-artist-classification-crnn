from setuptools import setup, find_packages

if __name__ == '__main__':
    with open('README.md') as fh:
        readme_contents = fh.read()

    setup(name='music_artist_classification_crnn',
          version='0.1',
          author='Zain Nasrullah',
          url='https://github.com/ZainNasrullah/music-artist-classification-crnn',

          description='Musical Artist Classification with Convolutional Recurrent Neural Networks',
          long_description=readme_contents,
          long_description_content_type='text/markdown',

          # describe the actual sources to distribute
          packages=find_packages('src'),
          package_dir={'': 'src'},

          # Describe dependencies.
          install_requires=[
              'Keras',
              'numpy',
              'scipy',
              'scikit-learn',
              'matplotlib',
              'librosa',
          ],
          )
