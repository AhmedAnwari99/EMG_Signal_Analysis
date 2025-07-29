
Explanation of some code snippets.



np.ones(30) creates an array of 30 ones → representing class 1 (“UP”).

np.zeros(30) creates an array of 30 zeros → representing class 0 (“DOWN”).




plt.plot(up_down_data.iloc[:, y==0], 'b')
plt.plot(up_down_data.iloc[:, y==1], 'r')


up_down_data mein say wo column /numbers/ select karo jou column numbers y mein 0 kay barabar (==) hain aur aunko label kar dou 'b' color say.
Similarly, up_down_data mein say wo column /numbers/ select karo jou column numbers y mein 1 kay barabar (==) hain aur auinko label kar dou 'r'.

Let's say df has columns 1 to 10.
y has 10 columns aswell.
first 5 columsn of y have value 0 and last five have value 1.

Select those column numbers from y in which value == 0. Use this column_numbers number to select columns from df. 
