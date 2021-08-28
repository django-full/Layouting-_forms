from django import forms

class contactForms(forms.Form):

    nama_lengkap       =forms.CharField(
        label='Nama Lengkap',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':'form-control col-sm-2',
                'id':'exampleInputEmail1',
                'aria-describedby':'emailHelp',
                'placeholder':'masukan nama'
            }
        )
    )




    tanggal_lahir      =forms.DateField(widget=forms.SelectDateWidget(
        attrs={
           'class':'form-control col-sm-2'

        },
        years=range(1990,2022,1)
    )
    )



    jenis_kelamin = forms.ChoiceField(
        choices=[('P','Pria'),
                    ('W', 'Wanita')
                  ],
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input'
            }
        )
    )


    email              =forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'masukan email'
        },


    ))
    alamat             =forms.TimeField(widget=forms.Textarea(
        attrs={


    }))
    aggre              =forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
        'class':'form-check-input'
    }),label="aggre_id")

button = forms


















