# Playing with heroes list

heroes = ['spider man','thor','hulk','iron man','captain america']

print('Length of the List is', len(heroes))

heroes.append('black panther')

heroes.remove('black panther')

thor_index = heroes.index('thor')
print(thor_index)
heroes.insert(thor_index+1, 'black panther')

# print(f'Now the super hero list becomes: {heroes}')

heroes[heroes.index('thor')] = 'doctor strange'
heroes[heroes.index('hulk')] = 'doctor strange'

heroes.sort()

print(f'Now the super hero list becomes: {heroes}')
