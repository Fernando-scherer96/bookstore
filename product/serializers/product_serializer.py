# Importando a classe 'serializers' da biblioteca 'rest_framework'.
from rest_framework import serializers

# Importando a classe 'Product' do módulo 'product' dentro do pacote 'Models'.
from product.Models.product import Product

# Importando 'CategorySerializer' do módulo 'serializers' dentro do pacote 'product'.
from product.serializers.category_serializer import CategorySerializer

# Definição da classe 'ProductSerializer' que herda de 'serializers.ModelSerializer'.
class ProductSerializer(serializers.ModelSerializer):
    # Definição de um campo serializado para categorias. 'CategorySerializer' é usado
    # para serializar cada categoria, e 'many=True' indica que pode haver múltiplas categorias.
    category = CategorySerializer(required=True, many=True)

    # Classe 'Meta' interna que fornece metadados adicionais para o 'ProductSerializer'.
    class Meta:
        # Especifica o modelo que o 'ProductSerializer' deve serializar, neste caso, 'Product'.
        model = Product
        # Define os campos que devem ser incluídos na serialização.
        fields = [
            'title',       # Título do produto
            'description', # Descrição do produto
            'price',       # Preço do produto
            'active',      # Status de atividade do produto (ativo ou não)
            'category',    # Categorias do produto, serializadas pelo 'CategorySerializer'
        ]
