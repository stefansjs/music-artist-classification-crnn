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
              'dill == 0.2.8.2',
              'h5py == 2.8.0',
              'Keras == 2.1.1',
              'librosa == 0.5.1',
              'matplotlib == 2.2.3',
              'numpy == 1.14.5',
              'pandas == 0.23.4',
              'scikit-learn == 0.20.0',
              'scipy == 1.1.0',
              'seaborn == 0.9.0',
              'tensorflow == 1.10.0',
          ],
          )
