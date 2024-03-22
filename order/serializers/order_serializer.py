# Importando a classe 'serializers' da biblioteca 'rest_framework'.
from rest_framework import serializers

# Importando a classe 'Product' do módulo 'Models' dentro do pacote 'product'.
from product.Models import Product

# Importando 'ProductSerializer' do módulo 'serializers' dentro do pacote 'product'.
from product.serializers.product_serializer import ProductSerializer

# Definição da classe 'OrderSerializer' que herda de 'serializers.ModelSerializer'.
class OrderSerializer(serializers.ModelSerializer):
    # Definição de um campo serializado para os produtos. 'ProductSerializer' é usado
    # para serializar cada produto, e 'many=True' indica que pode haver múltiplos produtos.
    product = ProductSerializer(required=True, many=True)
    
    # Definição de um campo serializado 'total' que será calculado usando um método específico.
    total = serializers.SerializerMethodField()

    # Método para calcular o valor total do pedido.
    # 'instance' representa a instância do modelo sendo serializado.
    def get_total(self, instance):
        # Calcula a soma dos preços de todos os produtos associados ao pedido.
        # 'instance.product.all()' retorna todos os produtos do pedido,
        # e a compreensão de lista é usada para somar seus preços.
        total = sum([product.price for product in instance.product.all()])
        return total
    
    # Classe 'Meta' interna que fornece metadados adicionais para o 'OrderSerializer'.
    class Meta:
        # Especifica o modelo que o 'OrderSerializer' deve serializar, neste caso, 'Product'.
        model = Product
        # Define os campos que devem ser incluídos na serialização.
        # Inclui 'product' e 'total' que foram definidos acima.
        fields = ['product', 'total']
